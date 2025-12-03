def delete_remaining_files(lab11_path):
    """
    Deletes all files (not folders) inside the All-Files directory.
    Keeps all folders such as:
        HCP-Dataset/
        Pet-Images/
        MRU-Fall2025/
    Does NOT delete anything inside subfolders.
    """
    import os
    from pathlib import Path

    lab11 = Path(lab11_path)
    all_files = lab11 / "All-Files"
    if not all_files.exists():
        raise FileNotFoundError(f"All-Files not found at {all_files}")

    for item in all_files.iterdir():
        if item.is_file():
            try:
                item.unlink()
            except Exception as e:
                # Continue even if one file fails
                pass

    return str(all_files)