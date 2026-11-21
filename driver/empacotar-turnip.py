"""Inspeciona e empacota o Turnip sem carregar a biblioteca."""
import argparse
import hashlib
import json
import re
import struct
import subprocess
import zipfile
from pathlib import Path


MESA_VERSION = "26.3.0"
SOURCE_SHA256 = "91d729aa68bb89e4ec857841300bbe922bcb3e52b1f97566ca83930d3b28343a"
DISPLAY_PATCH = "mesa-26.3.0-totk-display.patch"
PERFORMANCE_PATCH = "mesa-26.3.0-nplus-profiled.patch"
V4_PATCH = "mesa-26.3.0-nplus-v4.patch"
V5_PATCH = "mesa-26.3.0-nplus-v5.patch"
V6_PATCH = "mesa-26.3.0-nplus-v6.patch"
V7_PATCH = "mesa-26.3.0-nplus-v7.patch"


def package_metadata(mesa_version, library_name, variant):
    if variant == "v7":
        return {
            "schemaVersion": 1,
            "name": "n-plus-turnip-V7",
            "description": "Mesa Turnip 26.3.0 para Android ARM64 (Adreno 6xx/7xx/8xx): as correções do V6 (LRZ A8xx, IMapper5/UBWC, display) com ThinLTO experimental (allow-broken-lto do Mesa) para aliviar o custo de CPU do submit. Se algum jogo instabilizar, volte ao V6 no mesmo menu.",
            "author": "Mesa contributors / N+ Recomp",
            "packageVersion": "7",
            "vendor": "Mesa",
            "driverVersion": f"{mesa_version}-recomp.7",
            "minApi": 29,
            "libraryName": library_name,
        }
    if variant == "v6":
        return {
            "schemaVersion": 1,
            "name": "n-plus-turnip-V6",
            "description": "Mesa Turnip 26.3.0 para Android ARM64 (Adreno 6xx/7xx/8xx): velocidade do V5 + correção leve de LRZ A8xx (elimina piscadas no TOTK sem perda de FPS).",
            "author": "Mesa contributors / N+ Recomp",
            "packageVersion": "6",
            "vendor": "Mesa",
            "driverVersion": f"{mesa_version}-recomp.6",
            "minApi": 29,
            "libraryName": library_name,
        }
    if variant == "v5":
        return {
            "schemaVersion": 1,
            "name": "n-plus-turnip-V5",
            "description": "Mesa Turnip 26.3.0 para Android ARM64 (Adreno 6xx/7xx/8xx): IMapper5/UBWC + desempenho Adreno 830 restaurado (prefetch/LRZ).",
            "author": "Mesa contributors / N+ Recomp",
            "packageVersion": "5",
            "vendor": "Mesa",
            "driverVersion": f"{mesa_version}-recomp.5",
            "minApi": 29,
            "libraryName": library_name,
        }
    if variant == "v4":
        return {
            "schemaVersion": 1,
            "name": "n-plus-turnip-V4",
            "description": "Mesa Turnip 26.3.0 para Android ARM64 (Adreno 6xx/7xx/8xx): IMapper5/UBWC universal, correções Adreno 830 e API 29+.",
            "author": "Mesa contributors / N+ Recomp",
            "packageVersion": "4",
            "vendor": "Mesa",
            "driverVersion": f"{mesa_version}-recomp.4",
            "minApi": 29,
            "libraryName": library_name,
        }
    beta = variant == "v3-beta"
    return {
        "schemaVersion": 1,
        "name": "n-plus-turnip-V3-beta" if beta else "n-plus-turnip-V2",
        "description": (
            "Adreno 830: apresentação do V2 e seleção de renderização por tempo de GPU no Recomp."
            if beta else "Mesa Turnip para Android ARM64, com ajuste de apresentação de imagem para Adreno 830."
        ),
        "author": "Mesa contributors / N+ Recomp",
        "packageVersion": "3" if beta else "2",
        "vendor": "Mesa",
        "driverVersion": f"{mesa_version}-recomp.3-beta" if beta else f"{mesa_version}-recomp.2",
        "minApi": 34,
        "libraryName": library_name,
    }


def main(src, library, output, readelf, variant):
    beta = variant == "v3-beta"
    v4 = variant == "v4"
    v5 = variant == "v5"
    v6 = variant == "v6"
    v7 = variant == "v7"
    mesa_version = (src / "VERSION").read_text(encoding="utf-8").strip()
    if mesa_version != MESA_VERSION:
        raise ValueError(f"Esta receita requer Mesa {MESA_VERSION}, foi recebido {mesa_version}")
    library_bytes = library.read_bytes()
    if not 64 <= len(library_bytes) <= 128 << 20:
        raise ValueError("Tamanho fora do limite do importador")
    if library_bytes[:6] != b"\x7fELF\x02\x01" or struct.unpack_from("<HH", library_bytes, 16) != (3, 183):
        raise ValueError("O driver precisa ser um ELF64 AArch64 DYN")
    if v7:
        for marker in (
            b"N+ Turnip V7",
            b"N+ Turnip V7: Using IMapper v5 stable-C API",
            b"aimapper: compressed layout detected",
        ):
            if marker not in library_bytes:
                raise ValueError(f"O ELF V7 não contém o marcador esperado: {marker.decode('ascii')}")
    elif v6:
        for marker in (
            b"N+ Turnip V6",
            b"N+ Turnip V6: Using IMapper v5 stable-C API",
            b"aimapper: compressed layout detected",
        ):
            if marker not in library_bytes:
                raise ValueError(f"O ELF V6 não contém o marcador esperado: {marker.decode('ascii')}")
    elif v5:
        for marker in (
            b"N+ Turnip V5",
            b"N+ Turnip V5: Using IMapper v5 stable-C API",
            b"aimapper: compressed layout detected",
        ):
            if marker not in library_bytes:
                raise ValueError(f"O ELF V5 não contém o marcador esperado: {marker.decode('ascii')}")
    elif v4:
        for marker in (
            b"N+ Turnip V4",
            b"N+ Turnip V4: Using IMapper v5 stable-C API",
            b"aimapper: compressed layout detected",
        ):
            if marker not in library_bytes:
                raise ValueError(f"O ELF V4 não contém o marcador esperado: {marker.decode('ascii')}")
    else:
        if b"IMapper5 confirmed RGBA display buffer layout" not in library_bytes:
            raise ValueError("O ELF não contém o ajuste de apresentação do V2")
        beta_marker = b"N+ Turnip V3 beta" in library_bytes
        if beta != beta_marker or (not beta and b"N+ Turnip V2" not in library_bytes):
            raise ValueError(f"A identificação do ELF diverge da variante {variant}")
        if beta and any(marker not in library_bytes for marker in (
            b"profiled render-pass policy for nxnative on Adreno 830", b" / profiled",
        )):
            raise ValueError("O ELF beta não contém a identificação do perfil de desempenho")

    info = subprocess.check_output(
        [str(readelf), "--wide", "--dynamic", "--dyn-syms", "--program-headers", str(library)],
        text=True,
    )
    if not re.search(r"^\s*\d+:.*\bGLOBAL\s+DEFAULT\s+\d+\s+HMI\s*$", info, re.MULTILINE):
        raise ValueError("O driver não exporta o módulo HAL Vulkan do Android")
    if re.search(r"\((?:RUNPATH|RPATH)\)", info):
        raise ValueError("A biblioteca de distribuição ainda contém um caminho de busca da compilação")
    segments = re.findall(r"^\s*LOAD\s+[^\n]*?\s+(0x[0-9a-f]+)\s*$", info, re.MULTILINE)
    if not segments or min(int(align, 16) for align in segments) < 16384:
        raise ValueError("O driver não está alinhado para páginas de 16 KiB")
    dependencies = sorted(re.findall(r"Shared library: \[([^\]]+)\]", info))
    # The Vulkan HAL loads in the vendor namespace via libadrenotools.
    android_libraries = {
        "libandroid.so", "libc.so", "libdl.so", "libhardware.so",
        "liblog.so", "libm.so", "libnativewindow.so", "libsync.so", "libz.so",
    }
    if set(dependencies) - android_libraries:
        raise ValueError(f"Dependências inesperadas: {', '.join(dependencies)}")

    metadata = package_metadata(mesa_version, library.name, variant)
    digest = hashlib.sha256(library_bytes).hexdigest()
    patch_dir = Path(__file__).resolve().parent / "patches"
    patches = (V7_PATCH,) if v7 else (V6_PATCH,) if v6 else (V5_PATCH,) if v5 else (V4_PATCH,) if v4 else (DISPLAY_PATCH, PERFORMANCE_PATCH) if beta else (DISPLAY_PATCH,)
    api_label = "API 29" if (v4 or v5 or v6) else "API 34"
    patch_notes = "".join(
        f"Ajuste local {patch} (SHA-256 {hashlib.sha256((patch_dir / patch).read_bytes()).hexdigest()})\n"
        for patch in patches
    )
    notice = (
        f"Mesa Turnip {mesa_version}\n"
        f"Fonte oficial https://archive.mesa3d.org/mesa-{mesa_version}.tar.xz\n"
        f"SHA-256 da fonte {SOURCE_SHA256}\n"
        f"{patch_notes}"
        f"Android AArch64 / KGSL / {api_label} / NDK r28c\n"
        f"SHA-256 do ELF {digest}\n"
        f"Dependências Android {', '.join(dependencies)}\n"
        "Consulte LICENSE.Mesa.txt e NOTICE.NDK.txt para os avisos de origem.\n"
    )
    mesa_license = (src / "docs/license.rst").read_bytes()
    for license_file in sorted((src / "licenses").rglob("*")):
        if license_file.is_file():
            label = license_file.relative_to(src).as_posix().encode("ascii")
            mesa_license += b"\n\n" + label + b"\n\n" + license_file.read_bytes()
    ndk_notice = readelf.parent.parent / "NOTICE"
    destination = output / (metadata["name"] + ".zip")
    partial = destination.with_suffix(".zip.partial")
    readme_name = "LEIA-ME-V7.txt" if v7 else "LEIA-ME-V6.txt" if v6 else "LEIA-ME-V5.txt" if v5 else "LEIA-ME-V4.txt" if v4 else "LEIA-ME-V3-beta.txt" if beta else "LEIA-ME.txt"
    with zipfile.ZipFile(partial, "w", zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=False) as zip_out:
        zip_out.writestr("meta.json", json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
        zip_out.writestr(library.name, library_bytes)
        zip_out.write(output / readme_name, "README.txt")
        zip_out.writestr("LICENSE.Mesa.txt", mesa_license)
        zip_out.write(ndk_notice, "NOTICE.NDK.txt")
        zip_out.writestr("NOTICE.txt", notice)
    with zipfile.ZipFile(partial) as check:
        if check.testzip() is not None or check.getinfo(library.name).file_size != len(library_bytes):
            raise ValueError("O pacote gravado está incompleto")
    partial.replace(destination)
    package_digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    checksum_name = "SHA256-V7.txt" if v7 else "SHA256-V6.txt" if v6 else "SHA256-V5.txt" if v5 else "SHA256-V4.txt" if v4 else "SHA256-V3-beta.txt" if beta else "SHA256.txt"
    checksum = output / checksum_name
    checksum.write_text(f"{package_digest}  {destination.name}\n", encoding="ascii")
    print(f"{destination}\nSHA256 {package_digest}\nELF {digest}\nAndroid {', '.join(dependencies)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("src", "library", "output", "readelf"):
        parser.add_argument(name, type=Path)
    parser.add_argument("variant", choices=("v2", "v3-beta", "v4", "v5", "v6", "v7"), nargs="?", default="v7")
    main(**vars(parser.parse_args()))
