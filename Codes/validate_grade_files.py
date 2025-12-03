import os
from pathlib import Path
import csv


def validate_grade_files(lab11_path):
    """
    Checks each CSV in MRU-Fall2025 to ensure 30 rows.
    Prints:
      'All files are correct. No missing data.'
    or shows which files are incorrect.
    """

    lab11 = Path(lab11_path)
    mru_dir = lab11 / "All-Files" / "MRU-Fall2025"
    if not mru_dir.exists():
        raise FileNotFoundError("MRU-Fall2025 folder not found. Run move_grade_files first.")

    bad_files = []
    for csv_path in mru_dir.glob("*_grades.csv"):
        if not csv_path.is_file():
            continue
        with csv_path.open(newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            # Assume first row is header if any cell is non-numeric
            header_likely = bool(rows) and any(not cell.isdigit() for cell in rows[0])
            data_rows = rows[1:] if header_likely else rows
            # Count only non-empty rows
            data_rows = [r for r in data_rows if any(cell.strip() for cell in r)]
            if len(data_rows) != 30:
                bad_files.append(f"{csv_path.name} -> {len(data_rows)} rows")

    if not bad_files:
        print("All files are correct. No missing data.")
    else:
        print("Warning: The following files do not have exactly 30 rows:")
        for msg in bad_files:
            print(f" - {msg}")

    return bad_files