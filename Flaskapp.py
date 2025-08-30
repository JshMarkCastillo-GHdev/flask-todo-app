from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ["Learn Flask", "Build To-Do App", "Push to GitHub"]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

# This function is connected to the /add forms in index
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task") # get the input from the form
    if task: # If a task is added
        tasks.append(task) # add to the list
    return redirect(url_for("home")) # redirect to home

if __name__ == "__main__":
    app.run(debug=True)