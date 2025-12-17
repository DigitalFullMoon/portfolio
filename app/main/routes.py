# ======================================
# ROUTES DU BLUEPRINT MAIN
# ======================================
"""
Routes pour les pages publiques avec formatage serveur
"""

from flask import render_template, request, flash, redirect, url_for, jsonify
from app.main import bp
from app.main.forms import ContactForm, NewsletterForm
from app.models import Project, Contact, Newsletter
from app import db
import re


def format_nom(nom):
    """
    Formate le nom en MAJUSCULES
    Gère les espaces multiples
    """
    # Nettoyer les espaces multiples
    cleaned = ' '.join(nom.split())
    return cleaned.upper().strip()


def format_prenom(prenom):
    """
    Formate le prénom :
    - Première lettre de chaque mot en majuscule
    - Reste en minuscule
    - Gère les tirets ET les espaces
    Exemple: jean-pierre marie → Jean-Pierre Marie
    """
    prenom = prenom.strip()
    
    # D'abord, split sur les espaces
    words = prenom.split()
    formatted_words = []
    
    for word in words:
        # Pour chaque mot, split sur les tirets
        parts = word.split('-')
        # Capitalize chaque partie
        formatted_parts = [part.capitalize() for part in parts]
        # Rejoin avec tiret
        formatted_word = '-'.join(formatted_parts)
        formatted_words.append(formatted_word)
    
    # Rejoin avec espace
    return ' '.join(formatted_words)


def format_telephone(telephone):
    """
    Formate le téléphone : xx xx xx xx xx
    Exemple: 0612345678 → 06 12 34 56 78
    """
    if not telephone:
        return None
    
    # Nettoyer (enlever espaces, tirets, etc.)
    cleaned = re.sub(r'[^\d]', '', telephone)
    
    # Vérifier qu'on a bien 10 chiffres
    if len(cleaned) != 10:
        return None
    
    # Formater : xx xx xx xx xx
    return f"{cleaned[0:2]} {cleaned[2:4]} {cleaned[4:6]} {cleaned[6:8]} {cleaned[8:10]}"


# ======================================
# NOUVELLES ROUTES - PAGES SÉPARÉES
# ======================================

@bp.route('/')
@bp.route('/index')
@bp.route('/accueil')
def index():
    """
    Page d'accueil (ex: À propos)
    
    Route : /, /index, /accueil
    Template : main/accueil.html
    """
    return render_template('main/accueil.html')


@bp.route('/competences-experiences')
def competences_experiences():
    """
    Page Compétences & Expériences (même page, 2 sections)
    
    Route : /competences-experiences
    Template : main/competences_experiences.html
    Accessible aussi via /competences et /experiences avec ancres
    """
    return render_template('main/competences_experiences.html')


# Alias pour accéder directement aux sections avec ancres
@bp.route('/competences')
def competences():
    """Redirect vers la section compétences"""
    return redirect(url_for('main.competences_experiences') + '#competences')


@bp.route('/experiences')
def experiences():
    """Redirect vers la section expériences"""
    return redirect(url_for('main.competences_experiences') + '#experiences')


@bp.route('/projets')
def projets():
    """
    Page Projets (portfolio)
    
    Route : /projets
    Template : main/projets.html
    """
    # Tous les projets actifs, triés par ordre
    projects = Project.query.filter_by(
        is_active=True
    ).order_by(Project.order).all()
    
    return render_template('main/projets.html', projects=projects)


@bp.route('/blog')
def blog():
    """
    Page Blog (liste des articles)
    
    Route : /blog
    Redirige vers le blueprint blog
    """
    return redirect(url_for('blog.index'))


# ======================================
# ANCIENNES ROUTES (à supprimer après migration)
# ======================================

@bp.route('/portfolio')
def portfolio():
    """
    ANCIENNE ROUTE - Redirige vers /projets
    À garder pour compatibilité, sera supprimée plus tard
    """
    return redirect(url_for('main.projets'))


# ======================================
# ROUTE CONTACT (inchangée)
# ======================================

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Page de contact avec formulaire avancé
    
    Route : /contact
    Template : main/contact.html
    
    Formatage serveur :
    - NOM : MAJUSCULES
    - Prénom : Première-Lettre
    - Téléphone : xx xx xx xx xx
    - Email : validation stricte
    """
    form = ContactForm()
    
    if form.validate_on_submit():
        try:
            # ===================================
            # FORMATAGE DES DONNÉES
            # ===================================
            nom_formate = format_nom(form.nom.data)
            prenom_formate = format_prenom(form.prenom.data)
            telephone_formate = format_telephone(form.telephone.data) if form.telephone.data else None
            recrutement = form.recrutement.data == 'oui'
            
            # ===================================
            # CRÉATION DU CONTACT EN BDD
            # ===================================
            contact = Contact(
                nom=nom_formate,
                prenom=prenom_formate,
                email=form.email.data.lower().strip(),
                telephone=telephone_formate,
                recrutement=recrutement,
                newsletter_subscription=form.newsletter.data,
                message=form.message.data.strip()
            )
            
            db.session.add(contact)
            
            # ===================================
            # INSCRIPTION NEWSLETTER SI COCHÉE
            # ===================================
            if form.newsletter.data:
                # Vérifier si l'email n'est pas déjà inscrit
                existing_newsletter = Newsletter.query.filter_by(email=contact.email).first()
                
                if not existing_newsletter:
                    newsletter = Newsletter(
                        email=contact.email,
                        is_active=True
                    )
                    db.session.add(newsletter)
            
            # Sauvegarder en BDD
            db.session.commit()
            
            # ===================================
            # FLASH MESSAGE DE SUCCÈS
            # ===================================
            if recrutement:
                flash(
                    f'✅ Merci {prenom_formate} ! Votre candidature a bien été envoyée.',
                    'success'
                )
            else:
                flash(
                    f'✅ Merci {prenom_formate} pour votre message !',
                    'success'
                )
            
            # Redirection pour éviter la resoumission du formulaire
            return redirect(url_for('main.contact'))
            
        except Exception as e:
            # En cas d'erreur lors de la sauvegarde
            db.session.rollback()
            flash(
                '❌ Une erreur est survenue lors de l\'envoi du message.',
                'error'
            )
            print(f"Erreur contact form: {str(e)}")
    
    elif request.method == 'POST':
        # Le formulaire a été soumis mais n'est pas valide
        flash(
            '❌ Erreur dans le formulaire. Veuillez corriger les champs en rouge.',
            'error'
        )
    
    return render_template('main/contact.html', form=form)


@bp.route('/download-cv')
def download_cv():
    """
    Téléchargement du CV
    
    Route : /download-cv
    """
    # TODO: À implémenter plus tard
    flash('Fonctionnalité en cours de développement', 'info')
    return redirect(url_for('main.index'))