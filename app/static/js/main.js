// ======================================
// JAVASCRIPT PRINCIPAL
// ======================================

document.addEventListener('DOMContentLoaded', function() {
    
    // =====================================
    // MENU BURGER MOBILE
    // =====================================
    const burger = document.getElementById('navbarBurger');
    const mobileMenu = document.getElementById('navbarMobile');
    
    if (burger && mobileMenu) {
        burger.addEventListener('click', function() {
            // Toggle des classes
            mobileMenu.classList.toggle('is-active');
            burger.classList.toggle('is-active');
            
            // Empêcher le scroll du body quand le menu est ouvert
            if (mobileMenu.classList.contains('is-active')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });
        
        // Fermer le menu mobile quand on clique sur un lien
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenu.classList.remove('is-active');
                burger.classList.remove('is-active');
                document.body.style.overflow = '';
            });
        });
    }
    
    
    // =====================================
    // NAVBAR SCROLL EFFECT
    // =====================================
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Ajouter une ombre quand on scroll
        if (scrollTop > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScrollTop = scrollTop;
    });
    
    
    // =====================================
    // SMOOTH SCROLL POUR LES ANCRES
    // =====================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            
            // Ignore les liens # vides
            if (href === '#') return;
            
            const target = document.querySelector(href);
            
            if (target) {
                e.preventDefault();
                
                // Calculer la position en tenant compte de la navbar fixe
                const navbarHeight = navbar.offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navbarHeight - 20;
                
                // Smooth scroll
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    
    // =====================================
    // ANIMATION À L'APPARITION (SCROLL)
    // =====================================
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observer les éléments à animer
    const animateElements = document.querySelectorAll('.project-card, .about-content, .section-title');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    
    // =====================================
    // AUTO-HIDE FLASH MESSAGES
    // =====================================
    const flashMessages = document.querySelectorAll('.flash-message');
    
    flashMessages.forEach(message => {
        // Auto-hide après 5 secondes
        setTimeout(() => {
            message.style.animation = 'slideOutRight 0.3s ease-out forwards';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });
    
    // Animation de sortie
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(120%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    
    // =====================================
    // LAZY LOADING DES IMAGES
    // =====================================
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    
    // =====================================
    // FORMULAIRE NEWSLETTER (AJAX)
    // =====================================
    const newsletterForm = document.querySelector('.newsletter-form');
    
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const email = this.querySelector('input[type="email"]').value;
            const button = this.querySelector('button');
            const originalText = button.textContent;
            
            // Désactiver le bouton pendant la requête
            button.disabled = true;
            button.textContent = 'En cours...';
            
            // Envoyer la requête (à implémenter côté serveur)
            fetch(this.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email: email })
            })
            .then(response => response.json())
            .then(data => {
                // Afficher un message de succès
                showFlashMessage('Merci ! Tu es maintenant inscrit à la newsletter.', 'success');
                this.reset();
            })
            .catch(error => {
                showFlashMessage('Une erreur est survenue. Réessaie plus tard.', 'error');
            })
            .finally(() => {
                // Réactiver le bouton
                button.disabled = false;
                button.textContent = originalText;
            });
        });
    }
    
    
    // =====================================
    // FONCTION HELPER : AFFICHER FLASH MESSAGE
    // =====================================
    window.showFlashMessage = function(message, category = 'info') {
        const container = document.querySelector('.flash-messages') || createFlashContainer();
        
        const flashDiv = document.createElement('div');
        flashDiv.className = `flash-message flash-${category}`;
        flashDiv.innerHTML = `
            ${message}
            <button class="flash-close" onclick="this.parentElement.remove()">&times;</button>
        `;
        
        container.appendChild(flashDiv);
        
        // Auto-remove après 5 secondes
        setTimeout(() => {
            flashDiv.style.animation = 'slideOutRight 0.3s ease-out forwards';
            setTimeout(() => flashDiv.remove(), 300);
        }, 5000);
    };
    
    function createFlashContainer() {
        const container = document.createElement('div');
        container.className = 'flash-messages';
        document.body.appendChild(container);
        return container;
    }
    
    
    // =====================================
    // COPIER AU CLIPBOARD (utile pour code snippets)
    // =====================================
    window.copyToClipboard = function(text) {
        navigator.clipboard.writeText(text).then(() => {
            showFlashMessage('Copié dans le presse-papier !', 'success');
        }).catch(err => {
            showFlashMessage('Erreur lors de la copie', 'error');
        });
    };
    
    
    // =====================================
    // LOG DE BIENVENUE
    // =====================================
    console.log('%c🎨 Portfolio chargé avec succès!', 'color: #2563eb; font-size: 16px; font-weight: bold;');
    console.log('%cMode développement actif', 'color: #10b981;');
});


// =====================================
// UTILS : DEBOUNCE
// =====================================
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}