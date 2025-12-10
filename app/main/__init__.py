# ======================================
# BLUEPRINT MAIN - Pages publiques
# ======================================
"""
Ce blueprint gère les pages publiques :
- Homepage
- Portfolio
- Contact
"""

from flask import Blueprint

# Création du blueprint
# 'main' = nom du blueprint
# __name__ = nom du module Python
bp = Blueprint('main', __name__)

# Import des routes (à la fin pour éviter les imports circulaires)
from app.main import routes