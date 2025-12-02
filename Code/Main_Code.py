import os

# --------  MAIN PATH  --------
lab_path = "/Volumes/myData/MRU/2025-Fall-MRU/Labs/Lab-11-File-Manage/Lab-11"

# Path to the All-Files folder
all_files_path = os.path.join(lab_path, "All-Files")

# List items
items = os.listdir(all_files_path)

# Filter only files
files = [f for f in items if os.path.isfile(os.path.join(all_files_path, f))]

print("Files in folder:")
for f in files:
    print(f)
