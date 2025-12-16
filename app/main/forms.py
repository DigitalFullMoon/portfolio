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
    
    # Nom (obligatoire, que des lettres, espaces et -, formaté en MAJUSCULES)
    nom = StringField(
        'Nom',
        validators=[
            DataRequired(message='Le nom est requis'),
            Length(min=2, max=100, message='Le nom doit contenir entre 2 et 100 caractères')
        ],
        render_kw={
            'placeholder': 'DUPONT DE LA TOUR',
            'class': 'form-input',
            'autocomplete': 'family-name'
        }
    )
    
    # Prénom (obligatoire, min 2 lettres, espaces et accents autorisés)
    prenom = StringField(
        'Prénom',
        validators=[
            DataRequired(message='Le prénom est requis'),
            Length(min=2, max=100, message='Le prénom doit contenir au moins 2 caractères')
        ],
        render_kw={
            'placeholder': 'Jean-Pierre Marie',
            'class': 'form-input',
            'autocomplete': 'given-name'
        }
    )
    
    # Email (validation stricte avec regex)
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='L\'email est requis'),
            Email(message='Email invalide')
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
        validators=[Optional()],
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
    
    # Boutons
    submit = SubmitField('Envoyer', render_kw={'class': 'btn btn-primary'})
    
    
    def validate_nom(self, field):
        """Validation personnalisée du nom"""
        if not re.match(r'^[A-Za-zÀ-ÿ\s\-\']+$', field.data):
            raise ValidationError('Le nom ne peut contenir que des lettres, espaces, tiret (-) et apostrophe (\')')


    def validate_prenom(self, field):
        """Validation personnalisée du prénom"""
        if len(field.data) < 2:
            raise ValidationError('Le prénom doit contenir au moins 2 caractères')
        
        if not re.match(r'^[A-Za-zÀ-ÿ\s\-\']+$', field.data):
            raise ValidationError('Le prénom ne peut contenir que des lettres, espaces, tiret (-) et apostrophe (\')')
    
    
    def validate_telephone(self, field):
        """
        Validation personnalisée du téléphone
        Nettoie automatiquement les espaces et caractères non-numériques
        """
        if field.data and field.data.strip():
            # Nettoyer : garder uniquement les chiffres
            cleaned = ''.join(c for c in field.data if c.isdigit())
            
            # Vérifier la longueur
            if len(cleaned) > 0 and len(cleaned) != 10:
                raise ValidationError('Le téléphone doit contenir exactement 10 chiffres')
            
            # Mettre à jour avec la valeur nettoyée
            if len(cleaned) == 10:
                field.data = cleaned


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