# URL Shortener Service

A RESTful API for shortening URLs, built with **Flask** and **MongoDB**.

##  Features

- Create short URLs from long ones
- Retrieve original URLs using short codes
- Update existing URL mappings
- Delete short URLs
- Track and view access statistics
- Redirect users to the original URL

##  Tech Stack

- **Backend**: Python 3, Flask, Flask-RESTful
- **Database**: MongoDB
- **Dependencies**: `flask`, `flask-restful`, `pymongo`, `python-dotenv`

---


---

## 🚀 Getting Started

### 1. Clone the Repository

### 2. Create a Virtual Environment
#### Windows
python -m venv venv
venv\Scripts\activate

### 3.Install Dependencies
pip install -r requirements.txt

### 4. Configure Environment Variables
Create a .env file in the root directory:

MONGO_URI=mongodb://localhost:27017/
DB_NAME=url_shortener
BASE_URL=http://localhost:5000/

### 5. Run the Application
python app.py




