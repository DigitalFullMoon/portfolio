# ======================================
# INITIALISATION TEMPORAIRE DE FLASK
# ======================================
# Fichier minimal pour tester Docker

from flask import Flask

def create_app():
    """
    Factory function pour créer l'application Flask
    
    Pourquoi une factory function ?
    - Permet de créer plusieurs instances de l'app (pratique pour les tests)
    - Meilleure organisation du code
    - Pattern recommandé par Flask
    """
    
    # Création de l'instance Flask
    app = Flask(__name__)
    
    # Route de test
    @app.route('/')
    def hello():
        return """
        <h1>🎉 Flask fonctionne avec Docker !</h1>
        <p>Si tu vois ce message, Docker est bien configuré.</p>
        <p>Prochaine étape : configuration complète de Flask !</p>
        """
    
    return app