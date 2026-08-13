import os
import shutil

# JUST SOME BASICS FILE TYPES WHICH IT WILL GONNA SORT
file_types = {
    ".jpg": "Images", ".png": "Images",
    ".py": "Python code",
            ".cpp": "C++ Code",
            ".txt": "Documents", ".pdf": "Documents"
}

while True:
    source_folder = input(
        "Enter the folder path you want to organize : ").strip()

    if os.path.isdir(source_folder):
        break ;
    else :
        print("Wrong path! Please enter correct path : ")


destination_folder = input("Enter the destination folder path : ").strip()
files = os.listdir(source_folder)

for file in files:
    name, extension = os.path.splitext(file)

    full_path = os.path.join(source_folder, file)

    if os.path.isdir(full_path):
        continue

    category = file_types.get(extension, "Others")

    dest_folder = os.path.join(destination_folder, category)

    os.makedirs(dest_folder, exist_ok=True)

    dest_path = os.path.join(dest_folder , file)

    if os.path.isfile(dest_path):
        choice = input(f"{file} already exists.\n(r) Rename\n(o) Overwrite\n(s) Skip\nYour choice: ").strip().lower()

        move_file = True ; 
        
        if choice == "r" :
            new_name = input("Enter new name(with extension) : ").strip()
            dest_path = os.path.join(dest_folder , new_name)

        elif choice == "s" :
            move_file = False ;
            print(f"Skipped {file}") 
        
        if move_file :
            shutil.move(full_path , dest_path)
            print(f"Moved {file} --> {category}/")

    else : 
        shutil.move(full_path , dest_path)
        print(f"Moved {file} --> {category}/")
