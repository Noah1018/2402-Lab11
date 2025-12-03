def organize_hcp_files(lab11_path):
    """
    Inside HCP-Dataset, creates:
       Children/, Young/, Aged/
    Moves files based on:
       HCD → Children
       HCY → Young
       HCA → Aged
    """
    import os
    from pathlib import Path
    import shutil

    lab11 = Path(lab11_path)
    hcp_dir = lab11 / "All-Files" / "HCP-Dataset"
    if not hcp_dir.exists():
        raise FileNotFoundError("HCP-Dataset folder not found. Run move_hc_files first.")

    children = hcp_dir / "Children"
    young = hcp_dir / "Young"
    aged = hcp_dir / "Aged"
    children.mkdir(exist_ok=True)
    young.mkdir(exist_ok=True)
    aged.mkdir(exist_ok=True)

    for item in list(hcp_dir.iterdir()):
        if not item.is_file():
            continue
        name = item.name
        if name.startswith("HCD"):
            shutil.move(str(item), str(children / name))
        elif name.startswith("HCY"):
            shutil.move(str(item), str(young / name))
        elif name.startswith("HCA"):
            shutil.move(str(item), str(aged / name))

    return {
        "Children": str(children),
        "Young": str(young),
        "Aged": str(aged),
    }