from flask import render_template
from flask_login import login_required
from app.admin import bp


@bp.route('/')
@login_required
def index():
    return "<h1>Admin Dashboard</h1>"


@bp.route('/posts')
@login_required
def posts():
    return "<h1>Gestion des articles</h1>"