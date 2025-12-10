# ======================================
# ROUTES DE L'API
# ======================================
from flask import jsonify, request
from app.api import bp


@bp.route('/test')
def test():
    """Route de test de l'API"""
    return jsonify({
        'status': 'success',
        'message': 'API fonctionne correctement'
    })


@bp.route('/newsletter/subscribe', methods=['POST'])
def newsletter_subscribe():
    """Inscription à la newsletter (Brevo)"""
    # À implémenter plus tard
    return jsonify({
        'status': 'info',
        'message': 'Fonctionnalité en cours de développement'
    })


@bp.route('/recaptcha/verify', methods=['POST'])
def recaptcha_verify():
    """Vérification reCAPTCHA"""
    # À implémenter plus tard
    return jsonify({
        'status': 'info',
        'message': 'Fonctionnalité en cours de développement'
    })