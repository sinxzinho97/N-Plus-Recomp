#!/usr/bin/env bash
set -euo pipefail

mesa_version=26.3.0
mesa_sha256=91d729aa68bb89e4ec857841300bbe922bcb3e52b1f97566ca83930d3b28343a
ndk_version=r28c
ndk_sha1=a7b54a5de87fecd125a17d54f73c446199e72a64
android_api=34
jobs=${NPLUS_TURNIP_JOBS:-6}
lto=${NPLUS_TURNIP_LTO:-1}
mode=${1-package}
variant=${2-v6}
if [[ $# -gt 2 || ! "$mode" =~ ^(fetch|compile|package)$ ||
      ! "$variant" =~ ^(v2|v3-beta|v4|v5|v6|v7)$ || ! "$jobs" =~ ^[1-9][0-9]*$ || ! "$lto" =~ ^[01]$ ]]; then
    printf 'Usage: %s [fetch|compile|package] [v2|v3-beta|v4|v5|v6|v7] (positive NPLUS_TURNIP_JOBS, NPLUS_TURNIP_LTO=0|1)\n' "$0" >&2
    exit 2
fi
if [[ "$variant" == v4 || "$variant" == v5 || "$variant" == v6 || "$variant" == v7 ]]; then android_api=29; fi
recipe_dir=$(cd -- "$(dirname -- "$0")" && pwd -P)
v2_dir=$(realpath -m -- "${NPLUS_TURNIP_WORKDIR:-$HOME/.cache/nplus-recomp/turnip-$mesa_version}")
work_dir="$v2_dir"
if [[ "$variant" == v3-beta ]]; then work_dir="${v2_dir}-v3-beta"; fi
if [[ "$variant" == v4 ]]; then work_dir="${v2_dir}-v4"; fi
if [[ "$variant" == v5 ]]; then work_dir="${v2_dir}-v5"; fi
if [[ "$variant" == v6 ]]; then work_dir="${v2_dir}-v6"; fi
if [[ "$variant" == v7 ]]; then work_dir="${v2_dir}-v7"; fi
mkdir -p -- "$work_dir"
cd -- "$work_dir"
work_dir=$(pwd -P)
legacy_dir="$HOME/.cache/nplus-recomp/turnip-26.2.7"
src="mesa-$mesa_version"
ndk="android-ndk-$ndk_version"
ndk_cache="$work_dir"
for candidate in "$legacy_dir" "$v2_dir"; do
    if [[ -x "$candidate/$ndk/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android$android_api-clang" &&
          -f "$candidate/$ndk-linux.zip" ]] &&
       printf '%s  %s\n' "$ndk_sha1" "$candidate/$ndk-linux.zip" | sha1sum --check --status; then
        ndk_cache="$candidate"
        break
    fi
done

fetch_verified() {
    local url=$1 path=$2 digest=$3 hash_command=$4
    if [[ ! -f "$path" ]] || ! printf '%s  %s\n' "$digest" "$path" | "$hash_command" --check --status; then
        curl --fail --location --retry 3 --show-error --silent --connect-timeout 15 \
            --output "$path.partial" "$url"
        printf '%s  %s\n' "$digest" "$path.partial" | "$hash_command" --check
        mv -f -- "$path.partial" "$path"
    fi
    printf 'Verified %s\n' "$path"
}

archive="$work_dir/$src.tar.xz"
if [[ "$variant" != v2 && -f "$v2_dir/$src.tar.xz" ]] &&
   printf '%s  %s\n' "$mesa_sha256" "$v2_dir/$src.tar.xz" | sha256sum --check --status; then
    archive="$v2_dir/$src.tar.xz"
    printf 'Verified %s\n' "$archive"
else
    fetch_verified "https://archive.mesa3d.org/$src.tar.xz" "$archive" "$mesa_sha256" sha256sum
fi
if [[ "$ndk_cache" == "$work_dir" ]]; then
    fetch_verified "https://dl.google.com/android/repository/android-ndk-$ndk_version-linux.zip" \
        "$ndk-linux.zip" "$ndk_sha1" sha1sum
fi
if [[ "$mode" == fetch ]]; then exit 0; fi
ndk_bin="$ndk_cache/$ndk/toolchains/llvm/prebuilt/linux-x86_64/bin"
if [[ ! -x "$ndk_bin/aarch64-linux-android$android_api-clang" && "$ndk_cache" == "$work_dir" ]]; then
    unzip -oq "$ndk-linux.zip"
fi
cmp "$ndk_cache/$ndk/source.properties" <(unzip -p "$ndk_cache/$ndk-linux.zip" "$ndk/source.properties")
grep -Eq '^Pkg.Revision *= *28\.2\.13676358[[:space:]]*$' "$ndk_cache/$ndk/source.properties"

check_tools() {
    [[ -x "$1/bin/python" ]] && "$1/bin/python" -c \
        'from importlib.metadata import version; import sys; sys.exit(any(version(k) != v for k,v in {"meson":"1.9.0","Mako":"1.3.10","MarkupSafe":"3.0.3","packaging":"25.0","PyYAML":"6.0.2"}.items()))' 2>/dev/null
}
tool_dir="$legacy_dir/tools"
if ! check_tools "$tool_dir"; then
    tool_dir="$work_dir/tools"
    if [[ ! -x "$tool_dir/bin/python" ]]; then python3 -m venv "$tool_dir"; fi
    if ! check_tools "$tool_dir"; then
        "$tool_dir/bin/python" -m pip install --disable-pip-version-check \
            'meson==1.9.0' 'Mako==1.3.10' 'MarkupSafe==3.0.3' 'packaging==25.0' 'PyYAML==6.0.2'
    fi
fi
export PATH="$tool_dir/bin:$PATH" PYTHONDONTWRITEBYTECODE=1

# Confirm the cached source matches the pinned tarball with exactly this variant's patches.
# Keep an existing build incremental by preserving the timestamps of unchanged files.
patch_files=("$recipe_dir/patches/mesa-$mesa_version-totk-display.patch")
if [[ "$variant" == v3-beta ]]; then
    patch_files+=("$recipe_dir/patches/mesa-$mesa_version-nplus-profiled.patch")
elif [[ "$variant" == v4 ]]; then
    patch_files=("$recipe_dir/patches/mesa-$mesa_version-nplus-v4.patch")
elif [[ "$variant" == v5 ]]; then
    patch_files=("$recipe_dir/patches/mesa-$mesa_version-nplus-v5.patch")
elif [[ "$variant" == v6 ]]; then
    patch_files=("$recipe_dir/patches/mesa-$mesa_version-nplus-v6.patch")
elif [[ "$variant" == v7 ]]; then
    patch_files=("$recipe_dir/patches/mesa-$mesa_version-nplus-v7.patch")
fi
stage=$(mktemp -d -- "$work_dir/verified-mesa.XXXXXXXX")
cleanup_stage() {
    if [[ "$stage" == "$work_dir"/verified-mesa.* && -d "$stage" ]]; then
        rm -rf -- "$stage"
    fi
}
trap cleanup_stage EXIT
tar -xf "$archive" -C "$stage"
compare_tree() {
    diff --brief --recursive --no-dereference --exclude=__pycache__ --exclude='*.pyc' --exclude=.wraplock "$stage/$src" "$src"
}
apply_local_patch() {
    patch --directory="$1" -p1 --batch --forward --fuzz=0 --no-backup-if-mismatch --input="$2"
}
for patch_file in "${patch_files[@]}"; do
    test -s "$patch_file"
    prefix_matches=false
    if [[ -d "$src" ]] && compare_tree >/dev/null; then prefix_matches=true; fi
    apply_local_patch "$stage/$src" "$patch_file"
    if [[ "$prefix_matches" == true ]]; then apply_local_patch "$src" "$patch_file"; fi
done
if [[ -d "$src" ]]; then
    compare_tree
else
    mv -T -- "$stage/$src" "$src"
fi
cleanup_stage
trap - EXIT

# Android's NDK provides libz but does not ship its pkg-config record.
# Isolate target dependencies from the x86-64 Ubuntu libraries.
mkdir -p -- "$PWD/pkgconfig"
cat >pkgconfig/zlib.pc <<'PC'
Name: zlib
Description: zlib provided by the Android NDK sysroot
Version: 1.2.3
Libs: -lz
PC
cat >android-aarch64.ini <<EOF
[binaries]
c = '$ndk_bin/aarch64-linux-android$android_api-clang'
cpp = '$ndk_bin/aarch64-linux-android$android_api-clang++'
ar = '$ndk_bin/llvm-ar'
strip = '$ndk_bin/llvm-strip'
pkg-config = '/usr/bin/pkg-config'

[built-in options]
c_link_args = ['-Wl,-z,max-page-size=16384']
cpp_link_args = ['-static-libstdc++', '-Wl,-z,max-page-size=16384']

[properties]
needs_exe_wrapper = true
pkg_config_libdir = '$PWD/pkgconfig'

[host_machine]
system = 'android'
cpu_family = 'aarch64'
cpu = 'armv8'
endian = 'little'
EOF

setup_args=()
if [[ -f build/build.ninja ]]; then setup_args+=(--reconfigure); fi
# ThinLTO across the driver: the submit path (descriptor sets, draws, render passes) is CPU-hot in
# heavy games. Mesa rejects b_lto by default (support policy: LTO bugs are hard to debug); the upstream
# allow-broken-lto option is the sanctioned experimental route. NPLUS_TURNIP_LTO=0 keeps the plain
# release build for comparison; a V7 that misbehaves on a game falls back to V6 in the same menu
lto_args=()
if [[ "$lto" == 1 ]]; then lto_args+=(-Db_lto=true -Db_lto_mode=thin -Dallow-broken-lto=true); fi
meson setup "${setup_args[@]}" build "$src" --cross-file android-aarch64.ini --buildtype release \
    --prefix /usr --libdir lib --wrap-mode=nofallback \
    -Dstrip=true -Dplatforms=android -Dplatform-sdk-version="$android_api" \
    -Dandroid-stub=true -Dandroid-libbacktrace=disabled -Degl=disabled \
    -Dgallium-drivers= -Dvulkan-drivers=freedreno -Dfreedreno-kmds=kgsl \
    -Dllvm=disabled -Dexpat=disabled -Dzlib=enabled -Dzstd=disabled -Dbuild-tests=false \
    "${lto_args[@]}"
ninja -C build -j "$jobs" src/freedreno/vulkan/{libvulkan_freedreno.so,freedreno_icd.armv8.json}
# Meson strips using the NDK and removes the build-only android_stub RUNPATH.
meson install -C build --no-rebuild --skip-subprojects --tags runtime --destdir "$work_dir/pack"
if [[ "$mode" == compile ]]; then exit 0; fi

python "$recipe_dir/empacotar-turnip.py" "$PWD/$src" \
    "$PWD/pack/usr/lib/libvulkan_freedreno.so" "$recipe_dir" \
    "$ndk_bin/llvm-readelf" "$variant"
