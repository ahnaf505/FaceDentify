# FaceDentify ✨

<a href="https://python.org">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg" height="30">
</a>
<a href="">
  <img src="https://forthebadge.com/images/featured/featured-built-with-love.svg" height="30">
</a>

<a href="">
  <img src="https://forthebadge.com/images/badges/open-source.svg" height="30">
</a>

Welcome to **FaceDentify**! This project is all about comparing faces 🕵️‍♂️ against a database, whether it's for personal collections or large-scale datasets. Using powerful facial recognition technology, it matches faces and stores important details like full names and unique IDs (UUIDs) in a simple-to-use `TinyDB` database. It’s fast, scalable, and includes handy tools like photo labeling 📸. Perfect for everything from security systems to personal fun!

*Want to help out? Contributions are welcome! Just submit a pull request 🚀.*

## 🎯 Features

- **Add New Faces**: Easily insert one or more faces into the database, along with their details.
- **Search Faces**: Find a face using a photo or a unique Face ID.
- **Delete Faces**: Remove faces from the database either by photo comparison or by using the Face ID.
- **Clear Database**: **Be careful!** This option will delete everything in the database.

## 📋 Menu Options

1. **Insert a New Face**: Upload an image and enter the person’s full name.
2. **Add Multiple Faces**: Use a JSON file to add several faces at once, including their details.
3. **Search by Photo**: Find a face in the database by uploading a picture.
4. **Search by ID**: Get details about a face using its unique Face ID.
5. **Delete by Photo**: Remove a face by uploading an image to compare.
6. **Delete by ID**: Delete a face using its Face ID.
7. **Clear Database**: **Warning**: This will delete all faces and data!

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/facedentify.git
   cd facedentify
   ```
2. Install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 How to Use

1. Run the program:
   ```bash
   python facedentify.py
   ```
2. Follow the easy on-screen instructions to interact with your face database!

## 🔧 Tools

1. **Image Labeler**: A simple tool to label images with a full name. Uses `tkinter` and `Pillow`. Just type the name and press enter (Best for small datasets, not recommended for production).
2. **Face Backup**: Back up or restore your entire face database to/from another directory.

---