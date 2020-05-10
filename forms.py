from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class CreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image Link (full path)', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients(one per line)', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    submit = SubmitField('Add Drink')

class EditForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image Link (full path)', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients(one per line)', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    submit = SubmitField('Edit Drink')

class Delete(FlaskForm):
    title = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Delete this Drink')