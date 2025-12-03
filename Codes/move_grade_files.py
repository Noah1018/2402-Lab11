def move_grade_files(lab11_path):
    """
    Creates MRU-Fall2025 inside All-Files.
    Moves all CSV files ending with '_grades.csv'.
    """
    import os
    from pathlib import Path
    import shutil
    import glob

    lab11 = Path(lab11_path)
    all_files = lab11 / "All-Files"
    mru_dir = all_files / "MRU-Fall2025"
    mru_dir.mkdir(exist_ok=True)

    # Use glob.glob("*_grades.csv") explicitly as requested
    for src_path in glob.glob(str(all_files / "*_grades.csv")):
        src = Path(src_path)
        if src.is_file():
            shutil.move(str(src), str(mru_dir / src.name))

    return str(mru_dir)