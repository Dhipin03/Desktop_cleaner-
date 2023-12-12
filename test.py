import os
import shutil
from pathlib import Path

def cleanup(folder):
    
    if folder == 'Downloads':
        folder_to_clean = Path.home() / 'Downloads'
    elif folder == 'Desktop':
        folder_to_clean = Path.home() / 'Desktop'
    else:
        folder_to_clean = Path.home() / 'Documents'

    
    organized = folder_to_clean / 'Organized'
    if not organized.exists():
        organized.mkdir()

   
    folder_files = [f for f in folder_to_clean.iterdir() if f.is_file()]

   
    for file_path in folder_files:
        file_type = file_path.suffix.lower()[1:]  

        
        type_folder = organized / file_type
        if not type_folder.exists():
            type_folder.mkdir()

        
        shutil.move(str(file_path), str(type_folder / file_path.name))

    print(f"{folder_to_clean} cleanup completed!")

if __name__ == "__main__":
    folder = input("Where You Want To Clean ?: ")
    cleanup(folder)
