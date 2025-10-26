from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

# Définir tasks en global
tasks = [
    {"id": 1, "title": "train", "done": False},
    {"id": 2, "title": "sleep", "done": True}
]

@app.route("/")
def home():
    return render_template('index.html', tasks=tasks)

@app.route("/add", methods=['POST','GET'])
def ajout():
    titre = request.form.get("title")
    if not titre:
        return redirect(url_for('home'))
    # Ajouter une nouvelle tâche
    tasks.append({"id": len(tasks) + 1, "title": titre, "done": False})
    return redirect(url_for('home'))

@app.route("/done/<int:task_id>")
def done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            break
    return redirect(url_for('home'))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
