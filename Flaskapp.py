from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask World!(inside venv)"

@app.route("/about")
def about():
    return "This is the About page (inside venv)."

if __name__ == "__main__":
    app.run(debug=True)