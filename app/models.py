# ======================================
# MODÈLES DE BASE DE DONNÉES
# ======================================
"""
Les modèles représentent les tables de ta base de données.

SQLAlchemy (ORM) traduit tes classes Python en tables SQL.
Tu n'écris plus de SQL, tu manipules des objets Python !

Exemple :
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    
    Au lieu de :
    INSERT INTO user (username, email) VALUES ('john', 'john@example.com');
"""

from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


# ======================================
# MODÈLE USER (Utilisateurs)
# ======================================
class User(UserMixin, db.Model):
    """
    Table des utilisateurs
    
    UserMixin : ajoute automatiquement les méthodes nécessaires pour Flask-Login
    (is_authenticated, is_active, is_anonymous, get_id)
    """
    
    __tablename__ = 'users'
    
    # Colonnes
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Rôle : 'visitor' ou 'admin'
    role = db.Column(db.String(20), nullable=False, default='visitor')
    
    # Statut du compte
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    # Dates
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_login = db.Column(db.DateTime)
    
    # Relations (liens avec d'autres tables)
    # backref='author' : permet d'accéder à l'auteur depuis un Post avec post.author
    # lazy='dynamic' : charge les données seulement quand nécessaire (performance)
    posts = db.relationship('Post', backref='author', lazy='dynamic', cascade='all, delete-orphan')
    comments = db.relationship('Comment', backref='author', lazy='dynamic', cascade='all, delete-orphan')
    
    
    def set_password(self, password):
        """
        Hash le mot de passe avant de le stocker
        
        Pourquoi hacher ?
        - Sécurité : même si la BDD est volée, les mots de passe sont illisibles
        - bcrypt : algorithme très sécurisé, lent volontairement (résiste au brute force)
        """
        self.password_hash = generate_password_hash(password)
    
    
    def check_password(self, password):
        """
        Vérifie si le mot de passe est correct
        
        Args:
            password (str): Mot de passe en clair entré par l'utilisateur
            
        Returns:
            bool: True si le mot de passe est correct
        """
        return check_password_hash(self.password_hash, password)
    
    
    def is_admin(self):
        """Vérifie si l'utilisateur est admin"""
        return self.role == 'admin'
    
    
    def __repr__(self):
        """Représentation en string (pratique pour le debug)"""
        return f'<User {self.username}>'


# ======================================
# MODÈLE POST (Articles de blog)
# ======================================
class Post(db.Model):
    """Table des articles de blog"""
    
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    
    # Slug : URL-friendly version du titre
    # Exemple : "Mon Super Article !" → "mon-super-article"
    slug = db.Column(db.String(200), unique=True, nullable=False, index=True)
    
    # Contenu HTML (vient de l'éditeur WYSIWYG)
    content = db.Column(db.Text, nullable=False)
    
    # Résumé court (pour la liste des articles)
    excerpt = db.Column(db.String(500))
    
    # Image mise en avant
    featured_image = db.Column(db.String(255))
    
    # Auteur (Foreign Key vers User)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Statut de publication
    published = db.Column(db.Boolean, default=False, nullable=False)
    
    # Dates
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    date_modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Compteur de vues (optionnel, pour les stats)
    views = db.Column(db.Integer, default=0)
    
    # Relations
    comments = db.relationship('Comment', backref='post', lazy='dynamic', cascade='all, delete-orphan')
    
    
    def __repr__(self):
        return f'<Post {self.title}>'


# ======================================
# MODÈLE COMMENT (Commentaires)
# ======================================
class Comment(db.Model):
    """Table des commentaires sur les articles"""
    
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    
    # Auteur du commentaire
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Article commenté
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    
    # Modération : par défaut, le commentaire n'est pas approuvé
    approved = db.Column(db.Boolean, default=False, nullable=False)
    
    # Dates
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    date_moderated = db.Column(db.DateTime)
    
    
    def __repr__(self):
        return f'<Comment by {self.author_id} on Post {self.post_id}>'


# ======================================
# MODÈLE PROJECT (Projets du portfolio)
# ======================================
class Project(db.Model):
    """Table des projets du portfolio"""
    
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    # Image du projet
    image_url = db.Column(db.String(255))
    
    # Liens
    github_url = db.Column(db.String(255))
    demo_url = db.Column(db.String(255))
    
    # Technologies utilisées (stocké en JSON : ['Python', 'Flask', 'MySQL'])
    technologies = db.Column(db.JSON)
    
    # Ordre d'affichage (pour trier les projets)
    order = db.Column(db.Integer, default=0)
    
    # Visibilité
    is_featured = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    
    # Date de création du projet (pas de la ligne BDD)
    project_date = db.Column(db.DateTime)
    
    # Date d'ajout en BDD
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    
    def __repr__(self):
        return f'<Project {self.title}>'


# ======================================
# MODÈLE NEWSLETTER (Abonnés newsletter)
# ======================================
class Newsletter(db.Model):
    """Table des abonnés à la newsletter"""
    
    __tablename__ = 'newsletter'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    
    # ID du contact chez Brevo (pour synchronisation)
    brevo_contact_id = db.Column(db.String(100))
    
    # Statut
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    # Dates
    date_subscribed = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    date_unsubscribed = db.Column(db.DateTime)
    
    
    def __repr__(self):
        return f'<Newsletter {self.email}>'

# ======================================
# MODÈLE CONTACT (Messages de contact)
# ======================================
class Contact(db.Model):
    """Table des messages de contact"""
    
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Informations du contact
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, index=True)
    telephone = db.Column(db.String(14))  # Format: xx xx xx xx xx
    
    # Recrutement
    recrutement = db.Column(db.Boolean, nullable=False, default=False)
    
    # Newsletter
    newsletter_subscription = db.Column(db.Boolean, default=False)
    
    # Message
    message = db.Column(db.Text, nullable=False)
    
    # Statut du message
    is_read = db.Column(db.Boolean, default=False)
    is_replied = db.Column(db.Boolean, default=False)
    
    # Dates
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    date_read = db.Column(db.DateTime)
    date_replied = db.Column(db.DateTime)
    
    # CV envoyé (si recrutement)
    cv_sent = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Contact {self.prenom} {self.nom} - {self.email}>'

# ======================================
# LOADER POUR FLASK-LOGIN
# ======================================
@login_manager.user_loader
def load_user(user_id):
    """
    Flask-Login utilise cette fonction pour recharger l'utilisateur depuis la session
    
    Pourquoi ?
    - À chaque requête, Flask-Login vérifie si l'utilisateur est connecté
    - Il a juste l'ID en session, il doit recharger l'objet User complet
    """
    return User.query.get(int(user_id))