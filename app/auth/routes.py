# ======================================
# ROUTES D'AUTHENTIFICATION
# ======================================

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.auth import bp
from app import db
from app.models import User
from datetime import datetime


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Page de connexion"""
    
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        flash('Fonctionnalité en cours de développement', 'info')
    
    return "<h1>Page de login - Template à créer</h1>"


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Page d'inscription"""
    
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        flash('Fonctionnalité en cours de développement', 'info')
    
    return "<h1>Page de register - Template à créer</h1>"


@bp.route('/logout')
def logout():
    """Déconnexion"""
    logout_user()
    flash('Tu as été déconnecté avec succès.', 'success')
    return redirect(url_for('main.index'))