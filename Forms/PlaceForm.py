 from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms import validators



class PlaceForm(FlaskForm):
    place_name = StringField("Name: ", [
        validators.DataRequired("Please enter name of place."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    place_adress = StringField("Adress: ", [
        validators.DataRequired("Please enter your place adress."),
        validators.Length(3, 100, "Name should be from 3 to 100 symbols")
    ])

    place_price = IntegerField("Price: ",[
        validators.DataRequired("Please enter your place price."),
        validators.NumberRange(1, 1000, "Name should be from 1 to 1000 symbols")
    ])

    submit = SubmitField("Save")

    def check_price(self):
        return bool(self.place_price.data > 0)