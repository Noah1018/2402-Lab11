def move_hc_files(lab11_path):
    """
    Creates HCP-Dataset inside All-Files.
    Moves all files starting with 'HC'.
    """
    import os
    from pathlib import Path
    import shutil
    import glob

    lab11 = Path(lab11_path)
    all_files = lab11 / "All-Files"
    hcp_dir = all_files / "HCP-Dataset"
    hcp_dir.mkdir(exist_ok=True)

    # Move files starting with HC* from All-Files root into HCP-Dataset using glob.glob
    for src_path in glob.glob(str(all_files / "HC*")):
        src = Path(src_path)
        if src.is_file():
            shutil.move(str(src), str(hcp_dir / src.name))

    return str(hcp_dir)