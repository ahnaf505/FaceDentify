# 🏷️ Image Labeler

## Overview

**Image Labeler** is a user-friendly tool designed to simplify the process of labeling images of faces. Instead of manually renaming each file, you can simply type the full name associated with the image, hit Enter, and the tool will automatically rename and move the image to a designated folder. This is particularly useful for organizing large collections of images.

## ✨ Features

- **🖥️ Simple and Intuitive Interface:** The tool uses a clean and straightforward interface that makes it easy to label images quickly.
- **🔄 Automatic Image Renaming:** Just type the full name and press Enter. The image will be renamed and moved to a designated folder automatically.
- **❗ Error Handling:** If no images are found in the source folder, the tool will notify you and close gracefully.
- **📦 Batch Processing:** Process multiple images in a single session, with the tool automatically progressing to the next image after labeling.

## ⚙️ Installation

1. **📥 Clone the Repository:**
   ```bash
   git clone https://github.com/ahnaf505/FaceDentify.git
   cd tools
   cd image_labeler
   ```

2. **📦 Install Required Dependencies:**
   - Ensure you have Python 3.x installed.
   - Install the required Python packages using pip:
     ```bash
     pip install Pillow
     ```

3. **📂 Prepare Your Directories:**
   - Create a directory named `faceimg` in the project root. Place all the images you want to label in this directory.
   - The tool will automatically create a directory to store the labeled images. This directory will be named `labeled_<unique_id>` where `<unique_id>` is a randomly generated identifier.

## 🚀 Usage

1. **▶️ Run the Tool:**
   ```bash
   python main.py
   ```

2. **🏷️ Labeling Images:**
   - The tool will display each image one by one.
   - Type the full name corresponding to the image in the provided textbox and press Enter.
   - The image will be renamed with the full name and moved to the `labeled_<unique_id>` directory.

3. **⚠️ Handling Errors:**
   - If the `faceimg` directory is empty or contains no supported image files (`.png`, `.jpg`, `.jpeg`), the tool will show an error message and close automatically.

## 🖼️ Supported File Formats

- `.png`
- `.jpg`
- `.jpeg`

## 📝 Example Workflow

1. **Before Running:**
   - Your `faceimg` directory contains the following files:
     ```
     faceimg/
     ├── image1.png
     ├── image2.png
     └── image3.png
     ```

2. **During Execution:**
   - The tool will display `image1.png`. You type `John Doe` and press Enter.
   - The file is renamed to `<fullname>__<random_id>.png` and moved to the `labeled_<unique_id>` directory.
   - A record is added onto the `labeldb_<random_id>.json` 
   - The next image (`image2.png`) is displayed for labeling, and so on.

3. **After Running:**
   - Your `labeled_<unique_id>` directory will contain:
     ```
     labeled_<unique_id>/
     ├── John Doe__<random_id>.png
     ├── Jane Smith__<random_id>.png
     └── Alan Turing__<random_id>.png
     ```

## 🤝 Contributing

Feel free to contribute by forking the repository and submitting pull requests. Issues and feature requests are also welcome!

---