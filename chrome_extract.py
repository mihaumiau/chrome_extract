from pathlib import Path
import subprocess
import os
import shutil

script_dir = Path(__file__).resolve().parent
temp_dir = Path(os.environ["TEMP"])

for msi_file in script_dir.glob("*.msi"):
    print(f"Extracting: {msi_file.name}...")

    output_dir = temp_dir / msi_file.name
    output_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run([
        "7z",
        "x",
        f"{msi_file}",
        f"-o{output_dir}",
        "-aoa"
    ], stdout=subprocess.DEVNULL, check=True)

    binary_file = output_dir / "Binary.GoogleChromeInstaller"

    subprocess.run([
        "7z",
        "x",
        f"{binary_file}",
        f"-o{output_dir}",
        "-aoa"
    ], stdout=subprocess.DEVNULL, check=True)

    updater_archive = output_dir / "updater.7z"

    subprocess.run([
        "7z",
        "x",
        f"{updater_archive}",
        f"-o{output_dir}",
        "-aoa"
    ], stdout=subprocess.DEVNULL, check=True)

    offline_path = output_dir / "bin" / "Offline"
    offline_sub_path = next(p for p in Path(str(offline_path)).iterdir() if p.is_dir())
    offline_sub_sub_path = next(p for p in Path(str(offline_sub_path)).iterdir() if p.is_dir())
    offline_installer = next(p for p in Path(str(offline_sub_sub_path)).iterdir() if p.is_file())

    subprocess.run([
        "7z",
        "x",
        str(offline_installer),
        f"-o{output_dir}",
        "-aoa"
    ], stdout=subprocess.DEVNULL, check=True)

    chrome_archive = offline_path = output_dir / "chrome.7z"

    subprocess.run([
        "7z",
        "x",
        str(chrome_archive),
        f"-o{output_dir}",
        "-aoa"
    ], stdout=subprocess.DEVNULL, check=True)

    binary_directory = offline_path = output_dir / "Chrome-bin"
    chrome_directory = next(p for p in Path(str(binary_directory)).iterdir() if p.is_dir())

    shutil.copytree(chrome_directory, script_dir / chrome_directory.name, dirs_exist_ok=True)
    shutil.rmtree(output_dir)
