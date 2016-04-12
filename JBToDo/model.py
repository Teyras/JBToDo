from flask_sqlalchemy import SQLAlchemy
from JBToDo import db

class Task (db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    deadline = db.Column(db.DateTime())

