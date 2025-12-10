# ======================================
# FORMULAIRES DU BLUEPRINT MAIN
# ======================================
"""
Formulaires pour les pages publiques
"""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    """
    Formulaire de contact
    
    FlaskForm inclut automatiquement la protection CSRF
    """
    
    name = StringField(
        'Nom',
        validators=[
            DataRequired(message='Le nom est requis'),
            Length(min=2, max=100, message='Le nom doit contenir entre 2 et 100 caractères')
        ]
    )
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='L\'email est requis'),
            Email(message='Email invalide')
        ]
    )
    
    subject = StringField(
        'Sujet',
        validators=[
            DataRequired(message='Le sujet est requis'),
            Length(min=5, max=200, message='Le sujet doit contenir entre 5 et 200 caractères')
        ]
    )
    
    message = TextAreaField(
        'Message',
        validators=[
            DataRequired(message='Le message est requis'),
            Length(min=10, max=2000, message='Le message doit contenir entre 10 et 2000 caractères')
        ]
    )
    
    submit = SubmitField('Envoyer')


class NewsletterForm(FlaskForm):
    """Formulaire d'inscription newsletter"""
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='L\'email est requis'),
            Email(message='Email invalide')
        ]
    )
    
    submit = SubmitField('S\'abonner')