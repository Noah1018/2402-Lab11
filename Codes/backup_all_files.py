def backup_all_files(lab11_path):
    """
    Creates BACKUP-All-Files inside Lab-11.
    Copies the entire All-Files folder.
    """
    import os
    from pathlib import Path
    import shutil

    lab11 = Path(lab11_path)
    all_files_src = lab11 / "All-Files"
    backup_dst = lab11 / "BACKUP-All-Files"

    if not all_files_src.exists() or not all_files_src.is_dir():
        raise FileNotFoundError(f"Source folder not found: {all_files_src}")

    if backup_dst.exists():
        # Remove existing backup to ensure a clean copy
        shutil.rmtree(backup_dst)

    shutil.copytree(all_files_src, backup_dst)

    return str(backup_dst)