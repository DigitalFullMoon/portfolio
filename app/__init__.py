# ======================================
# INITIALISATION DE L'APPLICATION FLASK
# ======================================
"""
Ce fichier initialise Flask et toutes ses extensions.

Pattern "Application Factory" :
- Permet de créer plusieurs instances de l'app (dev, prod, tests)
- Meilleure organisation du code
- Facilite les tests unitaires
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import config


# ======================================
# INITIALISATION DES EXTENSIONS
# ======================================
# On crée les extensions ici, mais on les "attache" à l'app plus tard
# Pourquoi ? Pour pouvoir créer plusieurs instances de l'app

# SQLAlchemy : ORM pour la base de données
db = SQLAlchemy()

# Flask-Migrate : gestion des migrations de BDD
migrate = Migrate()

# Flask-Login : gestion des sessions utilisateurs
login_manager = LoginManager()

# Flask-Bcrypt : hash des mots de passe
bcrypt = Bcrypt()


# ======================================
# FONCTION FACTORY
# ======================================
def create_app(config_name='default'):
    """
    Crée et configure l'application Flask
    
    Args:
        config_name (str): Nom de la configuration à utiliser
                          ('development', 'production', 'testing')
    
    Returns:
        Flask: Instance de l'application configurée
    """
    
    # Création de l'instance Flask
    app = Flask(__name__)
    
    # Chargement de la configuration
    # On récupère la config depuis config.py selon l'environnement
    config_name = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[config_name])
    
    
    # =====================================
    # INITIALISATION DES EXTENSIONS
    # =====================================
    # On "attache" les extensions à l'application
    
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    
    # Configuration de Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Page de login
    login_manager.login_message = 'Merci de te connecter pour accéder à cette page.'
    login_manager.login_message_category = 'info'
    
    
    # =====================================
    # ENREGISTREMENT DES BLUEPRINTS
    # =====================================
    """
    Les Blueprints sont des "modules" de ton application.
    Chaque Blueprint gère une partie spécifique (auth, blog, admin, etc.)
    
    Avantages :
    - Organisation du code (1 dossier = 1 fonctionnalité)
    - Réutilisabilité
    - Facilite le travail en équipe
    """
    
    # On va créer ces blueprints juste après
    # Pour l'instant, on importe un blueprint de test
    
    # Blueprint Main (pages publiques : home, portfolio, contact)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Blueprint Auth (login, register, logout)
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # Blueprint Blog (articles, commentaires)
    from app.blog import bp as blog_bp
    app.register_blueprint(blog_bp, url_prefix='/blog')
    
    # Blueprint Admin (backoffice)
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Blueprint API (Brevo, reCAPTCHA)
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    
    # =====================================
    # GESTIONNAIRES D'ERREURS
    # =====================================
    """
    Personnalisation des pages d'erreur
    """
    
    @app.errorhandler(403)
    def forbidden(error):
        """Page d'erreur 403 - Accès interdit"""
        return app.send_static_file('errors/403.html'), 403
    
    @app.errorhandler(404)
    def not_found(error):
        """Page d'erreur 404 - Page non trouvée"""
        return app.send_static_file('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Page d'erreur 500 - Erreur serveur"""
        # En cas d'erreur BDD, on rollback
        db.session.rollback()
        return app.send_static_file('errors/500.html'), 500
    
    
    # =====================================
    # CONTEXTE SHELL (pratique pour debug)
    # =====================================
    """
    Permet d'avoir accès aux modèles directement dans le shell Flask
    
    Tu pourras taper : flask shell
    Et utiliser directement : User, Post, db, etc.
    """
    @app.shell_context_processor
    def make_shell_context():
        from app import models
        return {
            'db': db,
            'User': models.User,
            'Post': models.Post,
            'Comment': models.Comment,
            'Project': models.Project,
            'Newsletter': models.Newsletter
        }
    
    
    return app


# Import des modèles (nécessaire pour Flask-Migrate)
from app import models