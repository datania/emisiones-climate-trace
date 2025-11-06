import shutil
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.error import HTTPError
from urllib.request import Request, urlopen

COUNTRY = "ESP"
BASE_HOST = "https://downloads.climatetrace.org"
VERSION_START = (4, 8, 0)
DATASETS: tuple[str, ...] = (
    "co2",
    "co2e_100yr",
    "co2e_20yr",
    "ch4",
    "n2o",
    "pm2_5",
    "vocs",
    "co",
    "nh3",
    "nox",
    "so2",
    "bc",
    "oc",
)
OUTPUT_ROOT = Path("data/raw")
REQUEST_TIMEOUT = 30


def format_version(version: tuple[int, int, int]) -> str:
    return f"v{version[0]}.{version[1]}.{version[2]}"


def version_exists(version: tuple[int, int, int]) -> bool:
    version_str = format_version(version)
    probe_url = (
        f"{BASE_HOST}/{version_str}/country_packages/{DATASETS[0]}/{COUNTRY}.zip"
    )
    try:
        request = Request(probe_url, method="HEAD")
        with urlopen(request, timeout=REQUEST_TIMEOUT):
            return True
    except HTTPError as exc:
        if exc.code == 404:
            return False
        raise


def get_latest_version(start: tuple[int, int, int]) -> str:
    latest: tuple[int, int, int] | None = None
    major = start[0]
    first_major = True
    while True:
        minor = start[1] if first_major else 0
        minor_found = False
        first_minor = True
        while True:
            patch = start[2] if first_major and first_minor else 0
            patch_found = False
            while version_exists((major, minor, patch)):
                latest = (major, minor, patch)
                patch_found = True
                patch += 1
            if not patch_found:
                break
            minor_found = True
            first_minor = False
            minor += 1
        if not minor_found:
            break
        first_major = False
        major += 1
    if latest is None:
        raise RuntimeError(f"No versions found starting from {format_version(start)}")
    return format_version(latest)


def fetch_zip(url: str, destination: Path) -> None:
    """Stream a remote ZIP file into destination."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    with (
        urlopen(url, timeout=REQUEST_TIMEOUT) as response,
        destination.open("wb") as fp,
    ):
        shutil.copyfileobj(response, fp)


def extract_zip(zip_path: Path, target_dir: Path) -> None:
    """Extract all files from zip_path into target_dir."""
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(target_dir)


def download_dataset(dataset: str, base_url: str) -> None:
    url = f"{base_url}/{dataset}/{COUNTRY}.zip"
    target_dir = OUTPUT_ROOT / dataset
    print(f"Downloading {dataset} → {target_dir}")
    with TemporaryDirectory() as tmp_dir:
        tmp_zip = Path(tmp_dir) / f"{COUNTRY}.zip"
        fetch_zip(url, tmp_zip)
        extract_zip(tmp_zip, target_dir)
    print(f"✓ {dataset}")


def main() -> None:
    version = get_latest_version(VERSION_START)
    base_url = f"{BASE_HOST}/{version}/country_packages"
    print(f"Using dataset version {version}")
    for dataset in DATASETS:
        download_dataset(dataset, base_url)


if __name__ == "__main__":
    main()
