 from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, HiddenField, IntegerField
from wtforms import validators


class PlaceFormEdit(FlaskForm):
    place_name = StringField("Name: ", [validators.Length(3, 20, "Name should be from 3 to 20 symbols")])
    place_adress = StringField("Place: ", [validators.Length(3, 100, "Name should be from 3 to 100 symbols")])
    place_price = IntegerField("Price: ", [validators.NumberRange(1, 1000, "Name should be from 1 to 1000 symbols")])


    submit = SubmitField("Save")

    def check_price(self):
        return bool(self.place_price.data > 0)