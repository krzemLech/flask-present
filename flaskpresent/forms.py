from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError

# additional function for validation of the price field, in case javascript fails.
def price_check(form, field):
    price = str(field.data)
    if not price.isnumeric():
        raise ValidationError('Cena tylko w liczbach')


class PresentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=20)])
    link = StringField('link')
    price = IntegerField('price', validators=[DataRequired(), price_check])
    submit = SubmitField('dodaj')