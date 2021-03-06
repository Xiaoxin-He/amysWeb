from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField, IntegerField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User, Product
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(message='Username')])
    password = PasswordField('Password',validators=[DataRequired(message='Password')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AddProductsForm(FlaskForm):

    product_name = StringField('Name of Product:')
    file = FileField('File')
    product_description = StringField('Description of Product:')
    product_price = StringField('Price of Product:')
    # picture = FileField('Update product Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Add Product')

class DeleteForm(FlaskForm):

    id = IntegerField('Id Number of Product to Remove:')

    submit = SubmitField('Remove Product')

class AdminLoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(message='Username')])
    password = PasswordField('Password',validators=[DataRequired(message='Password')])
    secret_key = PasswordField('Secret_key',validators=[DataRequired(message='admin secret_key')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

    # def __init__(self, original_username, *args, **kwargs):
    #     super(EditProfileForm, self).__init__(*args, **kwargs)
    #     self.original_username = original_username

    # def validate_username(self, username):
    #     if username.data != self.original_username:
    #         user = User.query.filter_by(username=self.username.data).first()
    #         if user is not None:
    #             raise ValidationError('Please use a different username.')

