from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Correo',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Resgistrarse')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ese usuario ya esta en uso. Elija otro por favor.')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Ese correo ya esta en uso. Elija otro por favor.')


class LoginForm(FlaskForm):
    email = StringField('Correo',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Contrasena', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Iniciar Sesion')


class UpdateAccoutForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Correo',
                        validators=[DataRequired(), Email()])
    picture = FileField('Actualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Actualizar')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Ese usuario ya esta en uso. Elija otro porfavor.')

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Ese correo ya esta en uso. Elija otro porfavor.')


class PostForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired()])
    content = TextAreaField('Contenido', validators=[DataRequired()])
    submit = SubmitField('Publicar')


class RequestResetForm(FlaskForm):
    email = StringField('Correo',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Reestablecer contrasena')
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is None:
            raise ValidationError('No hay cuenta con esa informacion. Cree una por favor.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Contrasena',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reestablecer Contrasena')















