 from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms import validators


class ContestFormEdit(FlaskForm):
    contest_name = StringField("Name: ", [
        validators.DataRequired("Please enter name of Contest."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    submit = SubmitField("Save")