# 🗄️ Backup Script

## Overview

**Backup Script** is a command-line tool designed to efficiently back up essential folders and files from your project directory. It utilizes a clean interface with a progress bar to keep you informed about the backup status. This tool is ideal for creating timestamped backups of your important data with minimal hassle.

## ✨ Features

- **📊 Real-Time Progress Bar:** Displays a progress bar with `tqdm` to keep track of the backup progress, making it easy to monitor the process.
- **📦 Timestamped Backups:** Automatically organizes your backups into directories with timestamps for easy management and retrieval.
- **❌ Auto-Exit:** The script exits automatically after the backup is completed, streamlining the process from start to finish.

## ⚙️ Installation

1. **📥 Clone the Repository:**
   ```bash
   git clone https://github.com/ahnaf505/FaceDentify.git
   cd tools
   cd face_backup
   ```

2. **📦 Install Required Dependencies:**
   - Ensure you have Python 3.x installed.
   - Install the required Python packages using pip:
     ```bash
     pip install tqdm
     ```

## 🚀 Usage

1. **▶️ Run the Backup Script:**
   ```bash
   python main.py
   ```

2. **📂 Backup Process:**
   - The script backs up the specified directories (`facedb`, `imgfacedb`) and the `fullnames.json` file from two directories above the script's location.
   - The backup is stored in a `backups` directory within the parent directory, organized by a timestamp.

3. **🔄 Restoring Backups:**
   - To restore a backup, simply copy the desired backup folder from `backups` back to its original location.

## 📝 Example Workflow

1. **Before Running:**
   - Your directory structure should look like this:
     ```
     parent_directory/
     ├── facedb/
     ├── imgfacedb/
     └── fullnames.json
     ```

2. **During Execution:**
   - The script prompts you to start the backup process. Once initiated, a progress bar displays the status.
   - The backup is saved in a new directory under `backups` with a timestamp:
     ```
     parent_directory/
     └── backups/
         └── backup_20240101_123456/
             ├── facedb/
             ├── imgfacedb/
             └── fullnames.json
     ```

3. **After Running:**
   - The script automatically exits once the backup is complete.

## 📂 Directory Structure

- **Source Folders:**
  - `facedb/`
  - `imgfacedb/`
- **Source File:**
  - `fullnames.json`
- **Backup Directory:**
  - `backups/`

## 🛠️ Dependencies

- `tqdm`: For the progress bar.

---