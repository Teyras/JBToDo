from flask import render_template, redirect, url_for, flash
from JBToDo import app
from JBToDo import db
from JBToDo.model import Task

@app.route('/')
def index():
    items = Task.query.filter(Task.completed == False).all()
    return render_template('show_items.html', items = items)

from JBToDo.forms import NewItemForm

@app.route('/new', methods = ("GET", "POST"))
def new():
    form = NewItemForm()
    if form.validate_on_submit():
        task = Task()
        task.title = form.title.data
        task.deadline = form.deadline.data
        task.completed= False
        db.session.add(task)
        db.session.commit()
        flash("Task {title} created".format(title = task.title))
        return redirect(url_for('index'))
    return render_template('new_item.html', form = form)

@app.route('/complete/<id>')
def complete(id):
    task = Task.query.filter(Task.id == id).one()
    task.completed = True
    db.session.commit()
    flash("Task {title} completed".format(title = task.title))
    return redirect(url_for('index'))
