# ======================================
# FORMULAIRES D'AUTHENTIFICATION
# ======================================

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    """Formulaire de connexion"""
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Se connecter')


class RegisterForm(FlaskForm):
    """Formulaire d'inscription"""
    
    username = StringField(
        'Nom d\'utilisateur',
        validators=[DataRequired(), Length(min=3, max=80)]
    )
    
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    
    password = PasswordField(
        'Mot de passe',
        validators=[DataRequired(), Length(min=8, message='Le mot de passe doit contenir au moins 8 caractères')]
    )
    
    password2 = PasswordField(
        'Confirmer le mot de passe',
        validators=[DataRequired(), EqualTo('password', message='Les mots de passe doivent correspondre')]
    )
    
    submit = SubmitField('S\'inscrire')
    
    
    def validate_username(self, username):
        """Vérifie que le username n'existe pas déjà"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Ce nom d\'utilisateur est déjà pris.')
    
    
    def validate_email(self, email):
        """Vérifie que l'email n'existe pas déjà"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Cet email est déjà enregistré.')