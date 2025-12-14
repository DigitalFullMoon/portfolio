// ======================================
// VALIDATION FORMULAIRE CONTACT
// Validation visuelle instantanée (rouge → vert)
// Messages d'erreur uniquement à la soumission
// ======================================

document.addEventListener('DOMContentLoaded', function() {
    
    const form = document.getElementById('contactForm');
    const btnCancel = document.getElementById('btnCancel');
    
    // Récupérer tous les champs
    const nomInput = document.getElementById('nom');
    const prenomInput = document.getElementById('prenom');
    const emailInput = document.getElementById('email');
    const telephoneInput = document.getElementById('telephone');
    const messageInput = document.getElementById('message');
    const recrutementInputs = document.querySelectorAll('input[name="recrutement"]');
    
    // Flag pour savoir si on a déjà tenté de soumettre
    let submitAttempted = false;
    
    // =====================================
    // RÈGLES DE VALIDATION
    // =====================================
    
    const validationRules = {
        nom: {
            regex: /^[A-Za-zÀ-ÿ\-]+$/,
            message: 'Le nom ne peut contenir que des lettres et le tiret (-)',
            required: true
        },
        prenom: {
            regex: /^[A-Za-zÀ-ÿ\-]{2,}$/,
            message: 'Le prénom doit contenir au moins 2 lettres (accents et - autorisés)',
            required: true
        },
        email: {
            regex: /^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9][a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
            message: 'Format d\'email invalide (ex: email@example.com)',
            required: true
        },
        telephone: {
            regex: /^\d{10}$/,
            message: 'Le téléphone doit contenir exactement 10 chiffres',
            required: false
        },
        message: {
            minLength: 10,
            maxLength: 2000,
            message: 'Le message doit contenir entre 10 et 2000 caractères',
            required: true
        }
    };
    
    // =====================================
    // INITIALISATION : Tous les champs en ROUGE
    // =====================================
    function initializeFields() {
        const allInputs = [nomInput, prenomInput, emailInput, telephoneInput, messageInput];
        allInputs.forEach(input => {
            if (input) {
                input.classList.add('invalid');
            }
        });
    }
    
    initializeFields();
    
    // =====================================
    // FORMATAGE + VALIDATION NOM
    // =====================================
    if (nomInput) {
        nomInput.addEventListener('input', function() {
            const value = this.value;
            const cleaned = value.replace(/[^A-Za-zÀ-ÿ\-]/g, '');
            
            // Formatage en MAJUSCULES en temps réel
            this.value = cleaned.toUpperCase();
            
            // Validation visuelle instantanée
            const isValid = validationRules.nom.regex.test(cleaned) && cleaned.length > 0;
            updateVisualValidation(this, isValid);
        });
        
        nomInput.addEventListener('blur', function() {
            this.value = this.value.trim().toUpperCase();
            const isValid = validationRules.nom.regex.test(this.value) && this.value.length > 0;
            updateVisualValidation(this, isValid);
        });
    }
    
    // =====================================
    // FORMATAGE + VALIDATION PRÉNOM
    // =====================================
    if (prenomInput) {
        prenomInput.addEventListener('input', function() {
            const value = this.value;
            const cleaned = value.replace(/[^A-Za-zÀ-ÿ\-]/g, '');
            this.value = cleaned;
            
            // Validation visuelle instantanée
            const isValid = validationRules.prenom.regex.test(cleaned);
            updateVisualValidation(this, isValid);
        });
        
        prenomInput.addEventListener('blur', function() {
            // Formatage : Première lettre en majuscule après chaque tiret
            const formatted = formatPrenom(this.value.trim());
            this.value = formatted;
            
            const isValid = validationRules.prenom.regex.test(formatted);
            updateVisualValidation(this, isValid);
        });
    }
    
    // =====================================
    // VALIDATION EMAIL
    // =====================================
    if (emailInput) {
        emailInput.addEventListener('input', function() {
            const value = this.value.trim();
            const isValid = validationRules.email.regex.test(value);
            updateVisualValidation(this, isValid);
        });
        
        emailInput.addEventListener('blur', function() {
            const value = this.value.trim();
            const isValid = validationRules.email.regex.test(value);
            updateVisualValidation(this, isValid);
        });
    }
    
    // =====================================
    // FORMATAGE + VALIDATION TÉLÉPHONE
    // =====================================
    if (telephoneInput) {
        telephoneInput.addEventListener('input', function() {
            // Nettoyer : ne garder que les chiffres
            const cleaned = this.value.replace(/\D/g, '');
            
            // Limiter à 10 chiffres
            const limited = cleaned.substring(0, 10);
            
            // Formatage : xx xx xx xx xx
            this.value = formatTelephone(limited);
            
            // Validation visuelle (optionnel : vide OU 10 chiffres)
            const isValid = limited.length === 0 || limited.length === 10;
            updateVisualValidation(this, isValid);
        });
        
        telephoneInput.addEventListener('blur', function() {
            const cleaned = this.value.replace(/\D/g, '');
            this.value = formatTelephone(cleaned);
            
            const isValid = cleaned.length === 0 || cleaned.length === 10;
            updateVisualValidation(this, isValid);
        });
    }
    
    // =====================================
    // VALIDATION MESSAGE
    // =====================================
    if (messageInput) {
        messageInput.addEventListener('input', function() {
            const value = this.value.trim();
            const length = value.length;
            
            const isValid = length >= validationRules.message.minLength && 
                          length <= validationRules.message.maxLength;
            
            updateVisualValidation(this, isValid);
        });
        
        messageInput.addEventListener('blur', function() {
            const value = this.value.trim();
            const length = value.length;
            
            const isValid = length >= validationRules.message.minLength && 
                          length <= validationRules.message.maxLength;
            
            updateVisualValidation(this, isValid);
        });
    }
    
    // =====================================
    // SOUMISSION DU FORMULAIRE
    // =====================================
    if (form) {
        form.addEventListener('submit', function(e) {
            submitAttempted = true;
            let hasErrors = false;
            
            // Valider tous les champs et afficher les erreurs
            if (!validateFieldWithError(nomInput, 'nom')) hasErrors = true;
            if (!validateFieldWithError(prenomInput, 'prenom')) hasErrors = true;
            if (!validateFieldWithError(emailInput, 'email')) hasErrors = true;
            
            // Téléphone (optionnel mais si rempli doit être valide)
            if (telephoneInput && telephoneInput.value.trim()) {
                const cleaned = telephoneInput.value.replace(/\D/g, '');
                if (cleaned.length !== 10) {
                    showError('error-telephone', validationRules.telephone.message);
                    updateVisualValidation(telephoneInput, false);
                    hasErrors = true;
                }
            }
            
            // Message
            if (!validateFieldWithError(messageInput, 'message')) hasErrors = true;
            
            // Recrutement
            const recrutementChecked = Array.from(recrutementInputs).some(input => input.checked);
            if (!recrutementChecked) {
                showError('error-recrutement', 'Veuillez sélectionner une option');
                hasErrors = true;
            }
            
            // Si erreurs, empêcher la soumission
            if (hasErrors) {
                e.preventDefault();
                
                // Scroll vers la première erreur
                const firstInvalid = form.querySelector('.invalid');
                if (firstInvalid) {
                    firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    firstInvalid.focus();
                }
                
                // Message global
                if (window.showFlashMessage) {
                    window.showFlashMessage('Veuillez corriger les erreurs du formulaire', 'error');
                }
            }
        });
    }
    
    // =====================================
    // BOUTON ANNULER
    // =====================================
    if (btnCancel) {
        btnCancel.addEventListener('click', function() {
            if (confirm('Êtes-vous sûr de vouloir annuler ? Toutes les données seront perdues.')) {
                form.reset();
                submitAttempted = false;
                
                // Retirer toutes les validations visuelles et remettre en rouge
                initializeFields();
                
                // Cacher tous les messages d'erreur
                hideAllErrors();
            }
        });
    }
    
    // =====================================
    // FONCTIONS HELPER
    // =====================================
    
    /**
     * Met à jour UNIQUEMENT la validation visuelle (bordure rouge/verte)
     * PAS de message d'erreur
     */
    function updateVisualValidation(field, isValid) {
        if (isValid) {
            field.classList.remove('invalid');
            field.classList.add('valid');
        } else {
            field.classList.remove('valid');
            field.classList.add('invalid');
        }
    }
    
    /**
     * Valide un champ ET affiche le message d'erreur (uniquement à la soumission)
     */
    function validateFieldWithError(field, fieldName) {
        if (!field) return true;
        
        const value = field.value.trim();
        const rules = validationRules[fieldName];
        
        if (!rules) return true;
        
        // Champ requis mais vide
        if (rules.required && !value) {
            showError(`error-${fieldName}`, 'Ce champ est requis');
            updateVisualValidation(field, false);
            return false;
        }
        
        // Validation regex
        if (rules.regex) {
            const isValid = rules.regex.test(value);
            if (!isValid) {
                showError(`error-${fieldName}`, rules.message);
                updateVisualValidation(field, false);
            }
            return isValid;
        }
        
        // Validation longueur (pour le message)
        if (rules.minLength || rules.maxLength) {
            const length = value.length;
            const isValid = (!rules.minLength || length >= rules.minLength) &&
                          (!rules.maxLength || length <= rules.maxLength);
            
            if (!isValid) {
                showError(`error-${fieldName}`, rules.message);
                updateVisualValidation(field, false);
            }
            return isValid;
        }
        
        return true;
    }
    
    /**
     * Affiche un message d'erreur sous un champ
     */
    function showError(errorId, message) {
        const errorDiv = document.getElementById(errorId);
        if (errorDiv) {
            errorDiv.textContent = message;
            errorDiv.classList.add('show');
        }
    }
    
    /**
     * Cache tous les messages d'erreur
     */
    function hideAllErrors() {
        const allErrors = form.querySelectorAll('.form-error');
        allErrors.forEach(error => {
            error.classList.remove('show');
            error.textContent = '';
        });
    }
    
    /**
     * Formate le prénom : Première-Lettre
     * Exemple: jean-pierre → Jean-Pierre
     */
    function formatPrenom(prenom) {
        if (!prenom) return '';
        
        return prenom.split('-')
            .map(part => part.charAt(0).toUpperCase() + part.slice(1).toLowerCase())
            .join('-');
    }
    
    /**
     * Formate le téléphone : xx xx xx xx xx
     * Exemple: 0612345678 → 06 12 34 56 78
     */
    function formatTelephone(digits) {
        if (!digits) return '';
        
        const parts = [];
        for (let i = 0; i < digits.length; i += 2) {
            parts.push(digits.substring(i, i + 2));
        }
        
        return parts.join(' ');
    }
    
    // =====================================
    // LOG
    // =====================================
    console.log('📧 Validation formulaire contact : Visuelle instantanée (rouge → vert)');
    console.log('📧 Messages d\'erreur : Uniquement à la soumission');
});