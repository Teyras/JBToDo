from flask import render_template
from JBToDo import app
from JBToDo.model import Task

@app.route('/')
def index():
    items = Task.query.all()
    return render_template('show_items.html', items = items)
