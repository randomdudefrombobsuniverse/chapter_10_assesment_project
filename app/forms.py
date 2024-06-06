from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep Me Logged In')
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email',validators=[DataRequired(), Length(1, 64),Email()] )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class AddProductForm(FlaskForm):
    """AddProduct Form"""
    product_name = StringField('Product Name', validators=[DataRequired(), Length(1, 64)])
    product_description = TextAreaField('Product Description',validators=[DataRequired(), Length(1, 64),Email()] )
    stock_available = SelectField('Stock Available', 
    choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5') ], validators=[DataRequired()])
    submit = SubmitField('AddProduct')
