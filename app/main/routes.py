# ======================================
# ROUTES DU BLUEPRINT MAIN
# ======================================
"""
Définition des routes pour les pages publiques
"""

from flask import render_template, request, flash, redirect, url_for
from app.main import bp
from app.models import Project


@bp.route('/')
@bp.route('/index')
def index():
    """
    Page d'accueil
    
    Route : / ou /index
    Template : main/home.html
    """
    # On récupère les projets mis en avant
    featured_projects = Project.query.filter_by(
        is_featured=True,
        is_active=True
    ).order_by(Project.order).limit(3).all()
    
    return render_template('main/home.html', projects=featured_projects)


@bp.route('/portfolio')
def portfolio():
    """
    Page portfolio avec tous les projets
    
    Route : /portfolio
    Template : main/portfolio.html
    """
    # Tous les projets actifs, triés par ordre
    projects = Project.query.filter_by(
        is_active=True
    ).order_by(Project.order).all()
    
    return render_template('main/portfolio.html', projects=projects)


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Page de contact avec formulaire
    
    Route : /contact
    Template : main/contact.html
    Methods : GET (afficher le form) et POST (traiter le form)
    """
    if request.method == 'POST':
        # On traitera le formulaire plus tard
        # Pour l'instant, juste un message
        flash('Merci pour ton message ! Je te répondrai bientôt.', 'success')
        return redirect(url_for('main.contact'))
    
    return render_template('main/contact.html')


@bp.route('/download-cv')
def download_cv():
    """
    Téléchargement du CV
    
    Route : /download-cv
    """
    # On implémentera le téléchargement plus tard
    flash('Fonctionnalité en cours de développement', 'info')
    return redirect(url_for('main.index'))