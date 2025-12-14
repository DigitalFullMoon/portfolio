# ======================================
# FORMULAIRES DU BLUEPRINT MAIN
# ======================================
"""
Formulaires pour les pages publiques avec validation avancée
"""

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Email, Length, ValidationError, Optional, Regexp
import re


class ContactForm(FlaskForm):
    """
    Formulaire de contact avancé avec validation stricte
    """
    
    # Nom (obligatoire, que des lettres et -, formaté en MAJUSCULES)
    nom = StringField(
        'Nom',
        validators=[
            DataRequired(message='Le nom est requis'),
            Length(min=2, max=100, message='Le nom doit contenir entre 2 et 100 caractères'),
            Regexp(
                r'^[A-Za-zÀ-ÿ\-]+$',
                message='Le nom ne peut contenir que des lettres et le tiret (-)'
            )
        ],
        render_kw={
            'placeholder': 'DUPONT',
            'class': 'form-input',
            'autocomplete': 'family-name'
        }
    )
    
    # Prénom (obligatoire, min 2 lettres, accents autorisés, format: Première-Lettre)
    prenom = StringField(
        'Prénom',
        validators=[
            DataRequired(message='Le prénom est requis'),
            Length(min=2, max=100, message='Le prénom doit contenir au moins 2 caractères'),
            Regexp(
                r'^[A-Za-zÀ-ÿ\-]+$',
                message='Le prénom ne peut contenir que des lettres et le tiret (-)'
            )
        ],
        render_kw={
            'placeholder': 'Jean-Pierre',
            'class': 'form-input',
            'autocomplete': 'given-name'
        }
    )
    
    # Email (validation stricte avec regex)
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='L\'email est requis'),
            Email(message='Email invalide'),
            Regexp(
                r'^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9][a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                message='Format d\'email invalide'
            )
        ],
        render_kw={
            'placeholder': 'email@example.com',
            'class': 'form-input',
            'type': 'email',
            'autocomplete': 'email'
        }
    )
    
    # Téléphone (optionnel, 10 chiffres)
    telephone = StringField(
        'Téléphone',
        validators=[
            Optional(),
            Regexp(
                r'^\d{10}$',
                message='Le téléphone doit contenir exactement 10 chiffres'
            )
        ],
        render_kw={
            'placeholder': '06 12 34 56 78',
            'class': 'form-input',
            'type': 'tel',
            'autocomplete': 'tel'
        }
    )
    
    # Recrutement (radio OUI/NON)
    recrutement = RadioField(
        'Recrutement prévu',
        choices=[('oui', 'Oui'), ('non', 'Non')],
        default='non',
        validators=[DataRequired(message='Veuillez sélectionner une option')],
        render_kw={'class': 'form-radio'}
    )
    
    # Message
    message = TextAreaField(
        'Message',
        validators=[
            DataRequired(message='Le message est requis'),
            Length(min=10, max=2000, message='Le message doit contenir entre 10 et 2000 caractères')
        ],
        render_kw={
            'placeholder': 'Votre message...',
            'class': 'form-textarea',
            'rows': 6
        }
    )
    
    # Newsletter
    newsletter = BooleanField(
        'S\'abonner aux nouveautés',
        default=False,
        render_kw={'class': 'form-checkbox'}
    )
    
    # reCAPTCHA (sera activé en production)
    # recaptcha = RecaptchaField()
    
    # Boutons
    submit = SubmitField('Envoyer', render_kw={'class': 'btn btn-primary'})
    
    
    def validate_nom(self, field):
        """
        Validation personnalisée du nom
        - Que des lettres et tirets
        - Sera formaté en MAJUSCULES côté serveur
        """
        if not re.match(r'^[A-Za-zÀ-ÿ\-]+$', field.data):
            raise ValidationError('Le nom ne peut contenir que des lettres et le tiret (-)')
    
    
    def validate_prenom(self, field):
        """
        Validation personnalisée du prénom
        - Min 2 lettres
        - Accents autorisés
        - Sera formaté avec majuscule initiale
        """
        if len(field.data) < 2:
            raise ValidationError('Le prénom doit contenir au moins 2 caractères')
        
        if not re.match(r'^[A-Za-zÀ-ÿ\-]+$', field.data):
            raise ValidationError('Le prénom ne peut contenir que des lettres et le tiret (-)')
    
    
    def validate_telephone(self, field):
        """
        Validation personnalisée du téléphone
        - Optionnel, mais si rempli : exactement 10 chiffres
        """
        if field.data:
            # Nettoyer les espaces
            cleaned = field.data.replace(' ', '')
            
            if not re.match(r'^\d{10}$', cleaned):
                raise ValidationError('Le téléphone doit contenir exactement 10 chiffres')


class NewsletterForm(FlaskForm):
    """Formulaire d'inscription newsletter (footer)"""
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='L\'email est requis'),
            Email(message='Email invalide')
        ],
        render_kw={
            'placeholder': 'Ton email',
            'type': 'email'
        }
    )
    
    submit = SubmitField('S\'abonner')