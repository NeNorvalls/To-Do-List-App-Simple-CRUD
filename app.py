from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-me"

# Database setup
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "tasks.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ---------- Model ----------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    is_done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"


# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            flash("Task title cannot be empty!", "danger")
        else:
            db.session.add(Task(title=title))
            db.session.commit()
            flash("Task added successfully!", "success")
        return redirect(url_for("index"))

    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)


@app.route("/toggle/<int:id>", methods=["POST"])
def toggle_task(id):
    task = Task.query.get_or_404(id)
    task.is_done = not task.is_done
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    task = Task.query.get_or_404(id)
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            flash("Task title cannot be empty!", "danger")
        else:
            task.title = title
            db.session.commit()
            flash("Task updated successfully!", "success")
            return redirect(url_for("index"))
    return render_template("edit.html", task=task)


@app.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "info")
    return redirect(url_for("index"))


if __name__ == "__main__":
    # Create the tables once before the server starts (Flask 3-safe)
    with app.app_context():
        db.create_all()

    app.run(debug=True)
