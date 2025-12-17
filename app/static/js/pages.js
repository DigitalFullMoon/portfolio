// ======================================
// JAVASCRIPT POUR LES NOUVELLES PAGES
// ======================================

document.addEventListener('DOMContentLoaded', function() {
    
    // =====================================
    // ANIMATION DES BARRES DE COMPÉTENCES
    // =====================================
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px'
    };
    
    const skillObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const skillLevel = entry.target.querySelector('.skill-level');
                if (skillLevel) {
                    // Animer la barre de progression
                    const width = skillLevel.style.width;
                    skillLevel.style.width = '0%';
                    
                    setTimeout(() => {
                        skillLevel.style.width = width;
                    }, 100);
                }
                
                // Ne plus observer une fois animé
                skillObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observer toutes les cartes de compétences
    const skillCards = document.querySelectorAll('.skill-card');
    skillCards.forEach(card => skillObserver.observe(card));
    
    
    // =====================================
    // ANIMATION FADE-IN AU SCROLL
    // =====================================
    const fadeInObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    // Éléments à animer
    const animateElements = document.querySelectorAll(
        '.strength-card, .timeline-item, .about-section, .tool-tag'
    );
    
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        fadeInObserver.observe(el);
    });
    
    
    // =====================================
    // SMOOTH SCROLL POUR LES ANCRES
    // (Déjà géré dans main.js mais on s'assure)
    // =====================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            
            if (href === '#') return;
            
            const target = document.querySelector(href);
            
            if (target) {
                e.preventDefault();
                
                const navbar = document.querySelector('.navbar');
                const navbarHeight = navbar ? navbar.offsetHeight : 0;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navbarHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    
    // =====================================
    // COMPTEUR ANIMÉ (Pour statistiques)
    // =====================================
    function animateCounter(element) {
        const target = parseInt(element.getAttribute('data-target'));
        const duration = 2000; // 2 secondes
        const step = target / (duration / 16); // 60 FPS
        let current = 0;
        
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current);
            }
        }, 16);
    }
    
    // Observer pour les compteurs
    const counterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    // Appliquer aux éléments avec data-target
    document.querySelectorAll('[data-target]').forEach(counter => {
        counterObserver.observe(counter);
    });
    
    
    // =====================================
    // LOG
    // =====================================
    console.log('📄 Pages JS chargé : animations activées');
});