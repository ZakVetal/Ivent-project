 from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.fields.html5 import DateField


class UserForm(FlaskForm):
    people_name = StringField("Name: ", [
        validators.DataRequired("Please enter your name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])
    people_email = StringField("Email: ", [
        validators.DataRequired("Please enter your name."),
        validators.Email("Wrong email format")
    ])

    people_birthday = DateField("Birthday: ", [validators.DataRequired("Please enter birthday.")])

    people_phone = StringField("Phone: ", [validators.DataRequired("Please enter your phone."),
                                         validators.Length(10)])

    submit = SubmitField("Save")

    def validate_birthday(self):
        return bool(self.people_birthday.data.year > 1900)