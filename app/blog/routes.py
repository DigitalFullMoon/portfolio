from flask import render_template
from app.blog import bp


@bp.route('/')
def index():
    return "<h1>Blog - En cours de développement</h1>"


@bp.route('/<slug>')
def post(slug):
    return f"<h1>Article : {slug}</h1>"