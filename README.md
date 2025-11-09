# To-Do List App

- A Flask-based web application that allows users to add, edit, delete, and mark daily tasks as complete.
- It demonstrates basic CRUD operations using Flask, SQLAlchemy, and Bootstrap 5 for a simple, responsive interface.

## 🧭 Overview
- To-Do List App provides a simple way to manage daily tasks.

## It includes:
Add, edit, and delete task functionality
Mark tasks as done or undone
SQLite database for persistent storage
Clean Bootstrap 5 interface
Flash messages for quick user feedback

```
🏗️ Project Structure
To-Do-List-App/
│
├── app.py               # Main Flask application
├── requirements.txt      # Dependencies list
│
├── tasks.db              # SQLite database (auto-generated)
│
├── templates/
│   ├── base.html         # Common layout (Bootstrap, Navbar, Flash)
│   ├── index.html        # Home page (task list + add form)
│   └── edit.html         # Edit task page
│
├── static/
│   └── css/
│       └── style.css     # Custom CSS styling
│
├── .venv/                # Virtual environment
└── README.md             # Project documentation
```

## ⚙️ Technologies Used
- Library	Purpose
- Flask	Web framework
- Flask-SQLAlchemy	ORM for managing the database
- SQLite	Lightweight local database
- Jinja2	Template engine for dynamic HTML
- Bootstrap 5	Front-end framework for styling
- Python 3.12	Programming language

## 🧩 Installation Guide
### Clone the Repository
- git clone https://github.com/NeNorvalls/To-Do-List-App-Simple-CRUD.git
- cd To-Do-List-App

### Install Dependencies
- pip install -r requirements.txt

### If you don’t have a requirements file, install manually:
- pip install flask flask_sqlalchemy

### Run the App
- python app.py

### Then open your browser and go to:
- 👉 http://127.0.0.1:5000

### 🧠 How It Works
📝 1. Add Task
-  Users can add new tasks from the home page (/).
- The title is saved in the SQLite database via SQLAlchemy.

✏️ 2. Edit Task
- Click Edit on a task to open /edit/<id>.
- Users can change the title, then save the update.

✅ 3. Toggle Complete
- Each task can be marked as done or not done.
- This toggles a Boolean field in the database.

🗑️ 4. Delete Task
- Click Delete to remove a task permanently from the database.

Flash messages confirm each action (success, update, delete, etc.).

### 🧱 Database Schema
- Field	Type	Description
- id	Integer	Primary key
- title	String(200)	Task name or description
- is_done	Boolean	Task completion status
- created_at	DateTime	Auto-generated timestamp

### 🎨 Front-End Design
- Built with Bootstrap 5 via CDN
- base.html handles layout and includes the navbar and message alerts
- Pages extend the base template using Jinja2 {% block content %}
- Tasks styled with cards and line-through text when completed
- Extra tweaks defined in static/css/style.css
