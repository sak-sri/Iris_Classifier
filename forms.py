from flask_wtf import FlaskForm
from wtforms import IntegerField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,NumberRange,InputRequired

class SubmitData(FlaskForm):
    sep_len=FloatField('Sepal Length (in cm)',validators=[InputRequired(),NumberRange(0.08)])
    sep_width=FloatField('Sepal Width (in cm)',validators=[InputRequired(),NumberRange(0.08)])
    pet_len=FloatField('Petal Length (in cm)',validators=[InputRequired(),NumberRange(0.08)])
    pet_width=FloatField('Petal Width (in cm)',validators=[InputRequired(),NumberRange(0.08)])
    submit=SubmitField('Submit')