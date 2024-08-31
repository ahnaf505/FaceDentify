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

Welcome to **FaceDentify**! This project is all about comparing faces 🕵️‍♂️ against a database, whether it's for personal collections or large-scale datasets. Using powerful facial recognition technology, it matches faces and stores important details like full names and unique UIDs (UUIDs) in a simple-to-use `TinyDB` database. It’s fast, scalable, and includes handy tools like photo labeling 📸. Perfect for everything from security systems to personal fun!

*Want to help out? Contributions are welcome! Just submit a pull request 🚀.*

## 🎯 Features

- **Add New Faces**: Easily insert one or more faces into the database, along with their details.
- **Search Faces**: Find a face using a photo or a unique Face UID.
- **Delete Faces**: Remove faces from the database either by photo comparison or by using the Face UID.
- **Clear Database**: This option will delete everything in the database.

## Table of Contents 📖

1. [Installation](#installation)
2. [Usage](#usage)
   - [Insert Single Face](#insert-single-face)
   - [Insert List of Faces](#insert-list-of-faces)
   - [Query Face from Image](#query-face-from-image)
   - [Query Face by ID](#query-face-by-id)
   - [Delete Face by Image](#delete-face-by-image)
   - [Delete Face by ID](#delete-face-by-id)
   - [Clear Entire Database](#clear-entire-database)
3. [Contributing](#contributing)

## Installation 🚀

To get started with FaceDentify, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ahnaf505/FaceDentify.git
   cd facedentify
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage 🛠️

Once the application is running, the GUI provides various options to interact with the database:

   ### Insert Single Face
   
   1. Click **Insert Single Face**.
   2. Select an image file.
   3. Enter the full name of the person.
   4. The face is encoded and stored in the database with a unique ID.
   
   ### Insert List of Faces
   
   1. Click **Insert List of Faces**.
   2. Select a JSON file formatted like this:
       ```json
       [
           {
               "full_name": "John Doe",
               "filepath": "path/to/image1.png"
           },
           {
               "full_name": "Jane Smith",
               "filepath": "path/to/image2.png"
           }
       ]
       ```
   3. The tool adds each face to the database.
   
   ### Query Face from Image
   
   1. Click **Query Face from Image**.
   2. Select an image to search for similar faces in the database.
   3. If a match is found, the corresponding Face ID and full name are displayed.
   
   ### Query Face by ID
   
   1. Click **Query Face by ID**.
   2. Enter the Face ID.
   3. Retrieve the associated full name and image.
   
   ### Delete Face by Image
   
   1. Click **Delete Face by Image**.
   2. Select an image to find and delete the corresponding face.
   
   ### Delete Face by ID
   
   1. Click **Delete Face by ID**.
   2. Enter the Face ID to remove all associated data.
   
   ### Clear Entire Database ⚠️
   
   1. Click **Clear Entire Database**.
   2. Follow the prompts to confirm this irreversible action.
   
## 🔧 Tools

1. **Image Labeler**: A simple tool to label images with a full name. Uses `tkinter` and `Pillow`. Just type the name and press enter (Best for small datasets, not recommended for production).
2. **Face Backup**: Back up or restore your entire face database to/from another directory.

---