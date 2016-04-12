from flask_wtf import Form
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class NewItemForm(Form):
    title = StringField('Title', validators = [DataRequired()])
    deadline = DateTimeField('Deadline', validators = [DataRequired()])
    save = SubmitField('Save')
