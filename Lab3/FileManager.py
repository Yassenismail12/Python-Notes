import os
import shutil

def get_valid_directory():
    while True:
        dir_path = input("Enter directory path: ").strip()
        if not dir_path:
            print("Error: Path cannot be empty. Please try again.")
            continue
        if os.path.isdir(dir_path):
            return dir_path
        else:
            print(f"Error: Directory '{dir_path}' does not exist. Please try again.")
            retry = input("Would you like to try a different path? (y/n): ").strip().lower()
            if retry != 'y':
                return None

def create_backup_folder(base_path):
    backup_path = os.path.join(base_path, 'backup')
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
        print(f"Created 'backup' folder at: {backup_path}")
    else:
        print(f"'backup' folder already exists at: {backup_path}")
    return backup_path

def find_txt_files(directory):
    txt_files = []
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isfile(full_path) and item.lower().endswith('.txt'):
            txt_files.append(full_path)
    return txt_files

def copy_files_to_backup(txt_files, backup_path):
    copied_count = 0
    for file_path in txt_files:
        try:
            filename = os.path.basename(file_path)
            destination = os.path.join(backup_path, filename)
            shutil.copy2(file_path, destination)
            copied_count += 1
            print(f"Copied: {filename}")
        except Exception as e:
            print(f"Error copying {filename}: {e}")
    return copied_count

def print_summary(total_files, copied_files):
    print("\n" + "="*60)
    print("BACKUP SUMMARY")
    print("="*60)
    print(f"Total .txt files found: {total_files}")
    print(f"Files successfully copied: {copied_files}")
    if copied_files < total_files:
        print(f"Files failed to copy: {total_files - copied_files}")
    print("="*60)

def execute_task():
    print("\nOS FILE MANAGER - Automated Backup\n")
    dir_path = get_valid_directory()
    if dir_path is None:
        print("\nOperation cancelled.")
        return
    print(f"\nWorking with directory: {dir_path}")
    backup_path = create_backup_folder(dir_path)
    print("\nSearching for .txt files...")
    txt_files = find_txt_files(dir_path)
    if len(txt_files) == 0:
        print("No .txt files found in the directory.")
        print_summary(0, 0)
        return
    print(f"Found {len(txt_files)} .txt file(s)")
    print("\nCopying files to backup folder...")
    copied_count = copy_files_to_backup(txt_files, backup_path)
    print_summary(len(txt_files), copied_count)
