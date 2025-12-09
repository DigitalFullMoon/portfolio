# ======================================
# ÉTAPE 1 : Choisir l'image de base
# ======================================
# On utilise Python 3.11 (version stable et récente)
# "slim" = version allégée sans packages inutiles
FROM python:3.11-slim

# ======================================
# ÉTAPE 2 : Définir le mainteneur (toi !)
# ======================================
LABEL maintainer="ton-email@example.com"

# ======================================
# ÉTAPE 3 : Installer les dépendances système
# ======================================
# On installe les packages nécessaires pour MySQL et autres
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
# ÉTAPE 4 : Définir le répertoire de travail
# ======================================
# Tous les fichiers seront dans /app à l'intérieur du container
WORKDIR /app

# ======================================
# ÉTAPE 5 : Copier requirements.txt
# ======================================
# On copie d'abord SEULEMENT requirements.txt
# Pourquoi ? Pour profiter du cache Docker
# Si requirements.txt ne change pas, Docker réutilise le cache
COPY requirements.txt .

# ======================================
# ÉTAPE 6 : Installer les dépendances Python
# ======================================
# --no-cache-dir = ne pas garder le cache pip (réduit la taille)
RUN pip install --no-cache-dir -r requirements.txt

# ======================================
# ÉTAPE 7 : Copier tout le code de l'app
# ======================================
# Le point (.) signifie "tout le contenu du dossier actuel"
COPY . .

# ======================================
# ÉTAPE 8 : Exposer le port
# ======================================
# Flask va écouter sur le port 5000
# EXPOSE ne publie pas réellement le port, c'est juste une documentation
EXPOSE 5000

# ======================================
# ÉTAPE 9 : Variable d'environnement
# ======================================
# Pour que Flask sache qu'il tourne en mode développement
ENV FLASK_APP=run.py
ENV PYTHONUNBUFFERED=1
# PYTHONUNBUFFERED=1 = affiche les logs immédiatement (pratique pour debug)

# ======================================
# ÉTAPE 10 : Commande de démarrage
# ======================================
# CMD = commande exécutée au démarrage du container
# --host=0.0.0.0 = écoute sur toutes les interfaces (nécessaire pour Docker)
# --port=5000 = port d'écoute
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]