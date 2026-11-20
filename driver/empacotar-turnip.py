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
V6_PATCH = "mesa-26.3.0-nplus-v6.patch"


def package_metadata(mesa_version, library_name):
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


def main(src, library, output, readelf):
    mesa_version = (src / "VERSION").read_text(encoding="utf-8").strip()
    if mesa_version != MESA_VERSION:
        raise ValueError(f"Esta receita requer Mesa {MESA_VERSION}, foi recebido {mesa_version}")
    library_bytes = library.read_bytes()
    if not 64 <= len(library_bytes) <= 128 << 20:
        raise ValueError("Tamanho fora do limite do importador")
    if library_bytes[:6] != b"\x7fELF\x02\x01" or struct.unpack_from("<HH", library_bytes, 16) != (3, 183):
        raise ValueError("O driver precisa ser um ELF64 AArch64 DYN")
    for marker in (
        b"N+ Turnip V6",
        b"N+ Turnip V6: Using IMapper v5 stable-C API",
        b"aimapper: compressed layout detected",
    ):
        if marker not in library_bytes:
            raise ValueError(f"O ELF V6 não contém o marcador esperado: {marker.decode('ascii')}")

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

    metadata = package_metadata(mesa_version, library.name)
    digest = hashlib.sha256(library_bytes).hexdigest()
    patch_dir = Path(__file__).resolve().parent / "patches"
    patch_digest = hashlib.sha256((patch_dir / V6_PATCH).read_bytes()).hexdigest()
    notice = (
        f"Mesa Turnip {mesa_version}\n"
        f"Fonte oficial https://archive.mesa3d.org/mesa-{mesa_version}.tar.xz\n"
        f"SHA-256 da fonte {SOURCE_SHA256}\n"
        f"Ajuste local {V6_PATCH} (SHA-256 {patch_digest})\n"
        "Android AArch64 / KGSL / API 29 / NDK r28c\n"
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
    with zipfile.ZipFile(partial, "w", zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=False) as zip_out:
        zip_out.writestr("meta.json", json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
        zip_out.writestr(library.name, library_bytes)
        zip_out.write(output / "LEIA-ME-V6.txt", "README.txt")
        zip_out.writestr("LICENSE.Mesa.txt", mesa_license)
        zip_out.write(ndk_notice, "NOTICE.NDK.txt")
        zip_out.writestr("NOTICE.txt", notice)
    with zipfile.ZipFile(partial) as check:
        if check.testzip() is not None or check.getinfo(library.name).file_size != len(library_bytes):
            raise ValueError("O pacote gravado está incompleto")
    partial.replace(destination)
    package_digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    checksum = output / "SHA256-V6.txt"
    checksum.write_text(f"{package_digest}  {destination.name}\n", encoding="ascii")
    print(f"{destination}\nSHA256 {package_digest}\nELF {digest}\nAndroid {', '.join(dependencies)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("src", "library", "output", "readelf"):
        parser.add_argument(name, type=Path)
    main(**vars(parser.parse_args()))
