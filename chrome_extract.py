import shutil
import subprocess
from pathlib import Path

script_dir = Path(__file__).resolve().parent

for zip_archive in script_dir.glob("*.zip"):
    print(f"Extracting: {zip_archive.name}...")

    output_dir = script_dir / f"{zip_archive.name}.out"
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        _ = subprocess.run([
            "7z",
            "x",
            f"{zip_archive}",
            f"-o{output_dir}",
            "-aoa"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        msi_file = output_dir / "Installers" / "GoogleChromeStandaloneEnterprise64.msi"

        _ = shutil.copy(output_dir / "Installers" / "GoogleChromeStandaloneEnterprise64.msi", str(script_dir / zip_archive.name) + ".msi")

        Path(zip_archive).unlink(missing_ok=True)
    except Exception as e:
        print(f"skipped: {zip_archive.name}")
    finally:
        shutil.rmtree(output_dir)

for msi_file in script_dir.glob("*.msi"):
    print(f"Extracting: {msi_file.name}...")

    output_dir = script_dir / f"{msi_file.name}.out"
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        _ = subprocess.run([
            "7z",
            "x",
            f"{msi_file}",
            f"-o{output_dir}",
            "-aoa"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        binary_file = output_dir / "Binary.GoogleChromeInstaller"

        _ = subprocess.run([
            "7z",
            "x",
            f"{binary_file}",
            f"-o{output_dir}",
            "-aoa"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        updater_archive = output_dir / "updater.7z"

        _ = subprocess.run([
            "7z",
            "x",
            f"{updater_archive}",
            f"-o{output_dir}",
            "-aoa"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        offline_path = output_dir / "bin" / "Offline"
        offline_sub_path = next(p for p in Path(str(offline_path)).iterdir() if p.is_dir())
        offline_sub_sub_path = next(p for p in Path(str(offline_sub_path)).iterdir() if p.is_dir())
        offline_installer = next(p for p in Path(str(offline_sub_sub_path)).iterdir() if p.is_file())

        _ = shutil.copy(offline_installer, str(script_dir / msi_file.name) + ".exe")

        Path(msi_file).unlink(missing_ok=True)
    except Exception as e:
        print(f"skipped: {msi_file.name}")
    finally:
        shutil.rmtree(output_dir)

for exe_file in script_dir.glob("*.exe"):
    print(f"Extracting: {exe_file.name}...")

    output_dir = script_dir / f"{exe_file.name}.out"
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        _ = subprocess.run([
            "7z",
            "x",
            str(exe_file),
            f"-o{output_dir}",
            "-aoa"
        ], stdout=subprocess.DEVNULL, check=True)

        chrome_archive = next(p for p in Path(str(output_dir)).iterdir() if p.is_file())

        _ = subprocess.run([
            "7z",
            "x",
            str(chrome_archive),
            f"-o{output_dir}",
            "-aoa"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        binary_directory = next(p for p in Path(str(output_dir)).iterdir() if p.is_dir())
        chrome_directory = next(p for p in Path(str(binary_directory)).iterdir() if p.is_dir())

        _ = shutil.copytree(chrome_directory, script_dir / chrome_directory.name, dirs_exist_ok=True)

        Path(exe_file).unlink(missing_ok=True)
    except Exception as e:
        print(f"skipped: {exe_file.name}")
    finally:
        shutil.rmtree(output_dir)
