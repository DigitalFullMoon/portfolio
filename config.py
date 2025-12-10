# ======================================
# CONFIGURATION DE L'APPLICATION FLASK
# ======================================
"""
Ce fichier centralise toute la configuration de l'application.

Pourquoi faire ça ?
- Organisation : toute la config au même endroit
- Sécurité : les secrets viennent du fichier .env
- Flexibilité : facile de créer des configs différentes (dev, prod, test)
"""

import os
from datetime import timedelta

# Charge les variables du fichier .env
from dotenv import load_dotenv
load_dotenv()


class Config:
    """
    Configuration de base partagée par tous les environnements
    """
    
    # =====================================
    # CONFIGURATION FLASK
    # =====================================
    # Clé secrète pour sécuriser les sessions et les formulaires (CSRF)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Active la protection CSRF (Cross-Site Request Forgery)
    WTF_CSRF_ENABLED = True
    
    # Durée de vie des sessions (30 jours)
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
    
    
    # =====================================
    # CONFIGURATION BASE DE DONNÉES
    # =====================================
    # URL de connexion à MySQL
    # Format : mysql+pymysql://user:password@host:port/database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://portfolio_user:password@db:3306/portfolio_db'
    
    # Désactive le tracking des modifications (performance)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Pool de connexions : nombre de connexions simultanées
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,        # 10 connexions max
        'pool_recycle': 3600,   # Renouvelle les connexions toutes les heures
        'pool_pre_ping': True   # Vérifie que la connexion est active avant utilisation
    }
    
    
    # =====================================
    # CONFIGURATION UPLOAD DE FICHIERS
    # =====================================
    # Dossier où sont stockés les fichiers uploadés
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'app/static/uploads')
    
    # Taille maximum des fichiers (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    # Extensions autorisées pour les images
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    
    # Extensions autorisées pour les documents
    ALLOWED_DOCUMENTS = {'pdf', 'doc', 'docx'}
    
    
    # =====================================
    # CONFIGURATION BREVO (Newsletter)
    # =====================================
    BREVO_API_KEY = os.environ.get('BREVO_API_KEY')
    BREVO_LIST_ID = os.environ.get('BREVO_LIST_ID')
    
    
    # =====================================
    # CONFIGURATION GOOGLE reCAPTCHA
    # =====================================
    RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
    RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')
    
    # Active ou désactive reCAPTCHA (True en prod, False en dev pour tester plus vite)
    RECAPTCHA_ENABLED = True
    
    
    # =====================================
    # CONFIGURATION PAGINATION
    # =====================================
    # Nombre d'articles par page
    POSTS_PER_PAGE = 10
    
    # Nombre de commentaires par page
    COMMENTS_PER_PAGE = 20
    
    
    # =====================================
    # CONFIGURATION EMAIL (pour les notifications - optionnel)
    # =====================================
    # Tu pourras configurer ça plus tard si tu veux des notifications par email
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    
class DevelopmentConfig(Config):
    """
    Configuration pour l'environnement de développement
    """
    DEBUG = True
    TESTING = False
    
    # En dev, on peut désactiver reCAPTCHA pour aller plus vite
    RECAPTCHA_ENABLED = False


class ProductionConfig(Config):
    """
    Configuration pour l'environnement de production
    """
    DEBUG = False
    TESTING = False
    
    # En prod, reCAPTCHA est obligatoire
    RECAPTCHA_ENABLED = True
    
    # En prod, on force HTTPS pour les cookies de session
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'


class TestingConfig(Config):
    """
    Configuration pour les tests unitaires (on verra ça plus tard)
    """
    TESTING = True
    DEBUG = True
    
    # Base de données en mémoire pour les tests
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    
    # Désactive reCAPTCHA pour les tests
    RECAPTCHA_ENABLED = False
    
    # Désactive CSRF pour les tests
    WTF_CSRF_ENABLED = False


# =====================================
# DICTIONNAIRE DES CONFIGURATIONS
# =====================================
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}