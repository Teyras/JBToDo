from flask_wtf import Form
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired

class NewItemForm(Form):
    title = StringField('title', validators = [DataRequired()])
    deadline = DateTimeField('deadline', validators = [DataRequired()])
