import os
import shutil
import datetime
import curses
from tqdm import tqdm
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

source_folders = ['facedb', 'imgfacedb']
source_file = 'fullnames.json'

backup_dir = 'backups'
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = os.path.join(parent_dir, backup_dir, f'backup_{timestamp}')

os.makedirs(backup_path, exist_ok=True)

def copy_with_progress(src, dest, progress_bar):
    if os.path.isdir(src):
        shutil.copytree(src, dest)
    else:
        shutil.copy2(src, dest)
    progress_bar.update(1)

def backup_data(stdscr):
    total_items = len(source_folders) + 1
    progress_bar = tqdm(total=total_items, desc="Backing up", leave=False, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} ")

    for folder in source_folders:
        folder_src = os.path.join(parent_dir, folder)
        folder_dest = os.path.join(backup_path, folder)
        copy_with_progress(folder_src, folder_dest, progress_bar)
    
    file_src = os.path.join(parent_dir, source_file)
    file_dest = os.path.join(backup_path, source_file)
    copy_with_progress(file_src, file_dest, progress_bar)

    progress_bar.close()
    stdscr.addstr(10, 2, f"Backup completed successfully at {backup_path}")
    stdscr.refresh()
    
    print(f"Backup completed successfully at {backup_path}")
    sys.exit()

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(1, 1, "Press any key to start the backup...")
    stdscr.refresh()
    stdscr.getch()

    backup_data(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
