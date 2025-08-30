This is a sample Flask To Do Application.

This project has the basic CRUD operations (Create, Read, Update, Delete) and will serve as my introduction project in Flask Web development.

Features (Unfinished)
- Add tasks
- Mark tasks as complete
- Delete tasks
- Lastly, a basic web UI

Tech Stack used
- Backend: Python, Flask
- Frontend: HTML, Jinja2 Templates, CSS (basic)
- Database: SQLite (via SQLAlchemy)
- Tools: Git, Python Virtual Environment(venv)

Installation & Setup
# Clone repo
git@github.com:JshMarkCastillo-GHdev/flask-todo-app.git
cd flask-todo-app

# Create virtual environment
python -m venv venv

# Activate venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Running the App
# Start the development server:
python Flaskapp.py
# View the app here:
http://127.0.0.1:5000/
http://127.0.0.1:5000/about

# Project Structure
flask-todo-app/
│
├── app.py             # Main Flask app
├── requirements.txt   # Python dependencies
├── .gitignore         # Git ignore rules
└── venv/              # Virtual environment (ignored in Git)

# Contributions
For now this is a test app for learning purposes

# License
MIT License
