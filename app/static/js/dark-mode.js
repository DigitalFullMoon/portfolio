// ======================================
// DARK MODE - GESTION COMPLÈTE
// ======================================

/**
 * Initialisation du dark mode au chargement de la page
 * Vérifie la préférence sauvegardée ou utilise la préférence système
 */
document.addEventListener('DOMContentLoaded', function() {
    
    // Récupérer le toggle button
    const darkModeToggle = document.getElementById('darkModeToggle');
    
    if (!darkModeToggle) {
        console.warn('Dark mode toggle button not found');
        return;
    }
    
    // Vérifier si l'utilisateur a déjà une préférence sauvegardée
    const savedTheme = localStorage.getItem('theme');
    
    // Vérifier la préférence système de l'utilisateur
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // Appliquer le thème
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
    
    // Event listener sur le bouton toggle
    darkModeToggle.addEventListener('click', toggleDarkMode);
    
    // Détecter les changements de préférence système
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        // Ne change automatiquement que si l'utilisateur n'a pas de préférence explicite
        if (!localStorage.getItem('theme')) {
            if (e.matches) {
                enableDarkMode();
            } else {
                disableDarkMode();
            }
        }
    });
});

/**
 * Activer le dark mode
 */
function enableDarkMode() {
    document.body.classList.add('dark-mode');
    localStorage.setItem('theme', 'dark');
    
    // Animation de transition smooth
    document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
    
    // Log pour debug
    console.log('🌙 Dark mode activé');
}

/**
 * Désactiver le dark mode
 */
function disableDarkMode() {
    document.body.classList.remove('dark-mode');
    localStorage.setItem('theme', 'light');
    
    // Animation de transition smooth
    document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
    
    // Log pour debug
    console.log('☀️ Light mode activé');
}

/**
 * Toggle entre dark et light mode
 */
function toggleDarkMode() {
    if (document.body.classList.contains('dark-mode')) {
        disableDarkMode();
    } else {
        enableDarkMode();
    }
}

/**
 * Fonction publique pour forcer un thème (utile pour les tests)
 * Usage: setTheme('dark') ou setTheme('light')
 */
window.setTheme = function(theme) {
    if (theme === 'dark') {
        enableDarkMode();
    } else if (theme === 'light') {
        disableDarkMode();
    } else {
        console.error('Theme invalide. Utilisez "dark" ou "light"');
    }
};