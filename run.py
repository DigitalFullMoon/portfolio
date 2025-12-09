# ======================================
# POINT D'ENTRÉE DE L'APPLICATION
# ======================================
# Ce fichier démarre l'application Flask

# Import de l'application (dans app/__init__.py)
from app import create_app

# Création de l'instance de l'application
# create_app() est une "factory function"
app = create_app()

# ======================================
# DÉMARRAGE DU SERVEUR
# ======================================
if __name__ == '__main__':
    # Mode debug activé (hot-reload automatique)
    # host='0.0.0.0' = écoute sur toutes les interfaces (nécessaire pour Docker)
    # port=5000 = port d'écoute
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )