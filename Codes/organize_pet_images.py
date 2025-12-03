def organize_pet_images(lab11_path):
    """
    Creates Pet-Images folder inside All-Files.
    Creates Cat/ and Dog/ inside Pet-Images.
    Moves images based on filename containing 'cat' or 'dog'.
    """
    import os
    from pathlib import Path
    import shutil
    import re

    lab11 = Path(lab11_path)
    all_files = lab11 / "All-Files"
    pet_images = all_files / "Pet-Images"
    cat_dir = pet_images / "Cat"
    dog_dir = pet_images / "Dog"
    cat_dir.mkdir(parents=True, exist_ok=True)
    dog_dir.mkdir(parents=True, exist_ok=True)

    # Case-insensitive matching for 'cat' and 'dog' in filenames
    for item in all_files.iterdir():
        if not item.is_file():
            continue
        lower = item.name.lower()
        if "cat" in lower:
            shutil.move(str(item), str(cat_dir / item.name))
        elif "dog" in lower:
            shutil.move(str(item), str(dog_dir / item.name))

    return str(pet_images)