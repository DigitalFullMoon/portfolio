# ======================================
# L'image de base
# ======================================
# Python 3.11 (version stable et récente)
# "slim" = version allégée sans packages inutiles
FROM python:3.11-slim

# ======================================
# Définir le mainteneur
# ======================================
LABEL maintainer="ton-email@example.com"

# ======================================
# Installer les dépendances système
# ======================================
# Packages nécessaires pour MySQL et autres
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*
# gcc = compilateur C (pour certaines dépendances Python)
# default-libmysqlclient-dev = librairies MySQL
# pkg-config = outil de configuration
# rm -rf = on nettoie pour réduire la taille de l'image

# ======================================
# Définir le répertoire de travail
# ======================================
# Tous les fichiers seront dans /app à l'intérieur du container
WORKDIR /app

# ======================================
# Copier requirements.txt
# ======================================
# On copie requirements.txt
# Pourquoi ? Pour profiter du cache Docker
# Si requirements.txt ne change pas, Docker réutilise le cache
COPY requirements.txt .

# ======================================
# Installer les dépendances Python
# ======================================
# --no-cache-dir = ne pas garder le cache pip (réduit la taille)
RUN pip install --no-cache-dir -r requirements.txt

# ======================================
# Copier tout le code de l'app
# ======================================
# Le point (.) signifie "tout le contenu du dossier actuel"
COPY . .

# ======================================
# Exposer le port
# ======================================
# Flask va écouter sur le port 5000
EXPOSE 5000

# ======================================
# Variable d'environnement
# ======================================
# Pour que Flask sache qu'il tourne en mode développement
ENV FLASK_APP=run.py
ENV PYTHONUNBUFFERED=1
# PYTHONUNBUFFERED=1 = affiche les logs immédiatement 

# ======================================
# Commande de démarrage
# ======================================
# CMD = commande exécutée au démarrage du container
# --host=0.0.0.0 = écoute sur toutes les interfaces (nécessaire pour Docker)
# --port=5000 = port d'écoute
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]