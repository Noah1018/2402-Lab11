import os
from pathlib import Path

from backup_all_files import backup_all_files
from move_hc_files import move_hc_files
from organize_hcp_files import organize_hcp_files
from organize_pet_images import organize_pet_images
from move_grade_files import move_grade_files
from validate_grade_files import validate_grade_files
from delete_remaining_files import delete_remaining_files


def main():
    # Detect workspace Lab-11 path relative to this script
    lab11_path = Path(__file__).resolve().parents[1]  # assumes Codes/ is inside Lab-11/

    print(f"Lab-11 path: {lab11_path}")

    # Task 3: Backup All-Files
    backup_path = backup_all_files(str(lab11_path))
    print(f"Backup created at: {backup_path}")

    # Task 4: Move HC files
    hcp_path = move_hc_files(str(lab11_path))
    print(f"HCP-Dataset at: {hcp_path}")

    # Task 5: Organize HCP files
    hcp_subs = organize_hcp_files(str(lab11_path))
    print(f"Organized HCP into: {hcp_subs}")

    # Task 6: Organize Pet Images
    pet_images_path = organize_pet_images(str(lab11_path))
    print(f"Pet-Images at: {pet_images_path}")

    # Task 7: Move grade files
    mru_path = move_grade_files(str(lab11_path))
    print(f"MRU-Fall2025 at: {mru_path}")

    # Task 8: Validate grade files
    bad = validate_grade_files(str(lab11_path))
    if bad:
        print("Validation issues found.")

    # Task 9: Delete remaining files
    delete_remaining_files(str(lab11_path))
    print("Deleted loose files from All-Files.")


if __name__ == "__main__":
    main()
