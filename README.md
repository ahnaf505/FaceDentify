
# FaceDentify ✨

<a href="https://forthebadge.com">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg" height="30">
</a>
<a href="https://forthebadge.com">
  <img src="https://forthebadge.com/images/featured/featured-built-with-love.svg" height="30">
</a>


This project provides a robust solution for comparing a face against a database of any size, from small personal collections to large-scale datasets, using advanced facial recognition technology. The system efficiently matches faces and stores corresponding metadata, such as full names and random UUID, in a `TinyDB` database. Designed for scalability and optimized for performance, it also includes a few really useful tools, including photo labelling and etc., making it ideal for applications ranging from security systems to personal projects.

*If you would like to contribute to this project, please feel free to submit a pull request.*

## Features

- **Insert New Faces**: Add single or multiple faces to the database with associated metadata.
- **Query Faces**: Search the database for a face using biometric recognition or a Face ID.
- **Delete Faces**: Remove a face from the database either by biometric recognition or by Face ID.
- **Clear Database**: A high-risk operation that completely wipes all data from the database.

## Menu Options

1. **Insert a new single face into the database**: Load an image and input the subject's full name.
2. **Insert a list of faces into the database**: Load a JSON file containing multiple faces with their associated file paths and full names.
3. **Query face from biometric recognition**: Search for a face in the database using an image.
4. **Query face from Face ID**: Retrieve full name and face details using a unique Face ID.
5. **Delete face from biometric recognition**: Remove a face from the database by comparing it with an uploaded image.
6. **Delete face from Face ID**: Remove a face using its Face ID.
7. **Clear entire database**: **Dangerous operation** that deletes all faces and associated data.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/facedentify.git
   cd facedentify
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python facedentify.py
   ```
2. Follow the on-terminal instructions to interact with the database.

## Tools

1. coming soon

---