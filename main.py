import os
import shutil

# JUST SOME BASICS FILE TYPES WHICH IT WILL GONNA SORT
file_types = {
    ".jpg": "Images", ".png": "Images",
    ".py": "Python code",
            ".cpp": "C++ Code",
            ".txt": "Documents", ".pdf": "Documents"
}

# LISTS THE FILE IN THE GIVEN DIRECTORY
files = os.listdir("C:/Users/piyus/OneDrive/Desktop/Smart_Organizer")
print(files)

# NAMES ALL THE FILES WITH THIER EXTENSION IN THE GIVEN DIRECTORY
for file in files:
    name, extension = os.path.splitext(file)

    # IGNORES THE FOLDER ONLY FOCUS ON FILES
    full_path = os.path.join(
        "C:/Users/piyus/OneDrive/Desktop/Smart_Organizer", file)

    # IF FULL PATH FOUND THEN CONTINUES
    if os.path.isdir(full_path):
        continue
    print(file, "-->", extension)

    # IF THE FILE TYPES EXSISTS IT WILL TELL THE FILE TYPES OR IF IT DOES NOT THE IT WILL SIMPLY SAY IT BELONGS TO OTHERS
    category = file_types.get(extension, "Others")
    print(file, "belongs to", category)

    Destination_folder = os.path.join(
    "C:/Users/piyus/OneDrive/Desktop/Smart_Organizer_Destination", category)
    os.makedirs(Destination_folder, exist_ok=True)

    shutil.move(full_path , os.path.join(Destination_folder , file))
    print(f"Moved {file} --> {category}/")