-- ======================================
-- SCRIPT D'INITIALISATION DE LA BDD
-- ======================================
-- Ce script s'exécute automatiquement au premier démarrage de MySQL

-- Utiliser la base de données créée
USE portfolio_db;

-- ======================================
-- MESSAGE DE CONFIRMATION
-- ======================================
SELECT 'Base de données portfolio_db initialisée avec succès !' AS message;

-- Note : Les tables seront créées automatiquement par Flask-Migrate
-- Ce fichier est juste pour s'assurer que la BDD est bien créée
-- Tu pourras ajouter des données de test ici plus tard si tu veux