#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
import tempfile
import zipfile
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = PROJECT_ROOT / "gewitterradar-v4_05.zip"
FIXED_TIMESTAMP = (2026, 9, 7, 0, 0, 0)

ROOT_FILES = (
    "README.md",
    "CHANGELOG.md",
    "RELEASE_NOTES_V4_05.md",
    "SHA256SUMS.txt",
    "hacs.json",
    "gewitterradar-card-v4_05.js",
    "gewitterradar-card-v4_05.txt",
)
DIRECTORIES = ("dist", "docs", "home-assistant")

REQUIRED_ASSETS = {
    "gewitterradar-about-dedication-v4.webp",
    "gewitterradar-about-hero-v2.webp",
    "gewitterradar-brand-icon.png",
    "gewitterradar-compass-frame-v1.png",
    "gewitterradar-compass-frame-v2.png",
    "gewitterradar-compass-frame-v3.png",
    "gewitterradar-compass-frame-v4.png",
    "gewitterradar-compass-frame-v5.png",
    "gewitterradar-compass-selector-frame-v1.png",
    "gewitterradar-compass-selector-frame-v2.png",
    "gewitterradar-compass-selector-frame-v3.png",
    "gewitterradar-compass-selector-frame-v4.png",
    "gewitterradar-compass-selector-frame-v5.png",
    "gewitterradar-trend-arrow.png",
    "gewitterradar-trend-medallion.png",
}


def package_files() -> list[Path]:
    files = [PROJECT_ROOT / path for path in ROOT_FILES]
    for directory in DIRECTORIES:
        files.extend(path for path in (PROJECT_ROOT / directory).rglob("*") if path.is_file())
    return sorted(files, key=lambda path: path.relative_to(PROJECT_ROOT).as_posix())


def main() -> None:
    output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_OUTPUT
    output.parent.mkdir(parents=True, exist_ok=True)

    missing = [path for path in package_files() if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing release files: {missing}")

    with tempfile.NamedTemporaryFile(dir=output.parent, suffix=".zip", delete=False) as temporary:
        temporary_path = Path(temporary.name)

    try:
        with zipfile.ZipFile(temporary_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in package_files():
                relative_path = path.relative_to(PROJECT_ROOT).as_posix()
                info = zipfile.ZipInfo(relative_path, FIXED_TIMESTAMP)
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        os.replace(temporary_path, output)
    finally:
        temporary_path.unlink(missing_ok=True)

    with zipfile.ZipFile(output, "r") as archive:
        names = set(archive.namelist())
        required = {
            "dist/gewitterradar.js",
            "dist/app_gewitterradar_pkg.yaml",
            "home-assistant/app_gewitterradar_pkg.yaml",
            *(f"dist/assets/{asset}" for asset in REQUIRED_ASSETS),
        }
        absent = sorted(required - names)
        if absent:
            raise RuntimeError(f"Source ZIP is incomplete; missing: {absent}")

    print(
        f"Built internal V4.05 source ZIP {output} with {len(package_files())} files and "
        f"verified HACS card, {len(REQUIRED_ASSETS)} graphics and staged Home Assistant package."
    )


if __name__ == "__main__":
    main()
