 from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.fields.html5 import DateField


class EventForm(FlaskForm):
    event_name = StringField("Name: ", [
        validators.DataRequired("Please enter name of Event."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    event_date = DateField("Date: ", [validators.DataRequired("Please enter date of Event.")])


    submit = SubmitField("Save")

    def validate_date(self):
        return bool(self.event_date.data.year > 2018)