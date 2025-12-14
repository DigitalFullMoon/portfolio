# TODO LIST - Portfolio

## 📧 Emails Automatiques (Contact)

### Template Email - Candidature (recrutement = OUI)
- [ ] Créer template HTML pour email candidature
- [ ] Sujet : "Confirmation de votre candidature"
- [ ] Contenu : Remerciement + infos sur le processus
- [ ] PJ : CV à envoyer automatiquement
- [ ] Configurer envoi avec Flask-Mail ou service SMTP

### Template Email - Contact Standard (recrutement = NON)
- [ ] Créer template HTML pour email remerciement
- [ ] Sujet : "Merci pour votre message"
- [ ] Contenu : Accusé de réception + délai de réponse
- [ ] PJ : CV à envoyer automatiquement
- [ ] Configurer envoi avec Flask-Mail ou service SMTP

## 🔐 Sécurité & Intégrations

- [ ] Activer Google reCAPTCHA en production
  - Obtenir clés API sur https://www.google.com/recaptcha/admin
  - Intégrer dans formulaire contact
  - Validation côté serveur

- [ ] Configurer Brevo (Newsletter)
  - API Key à obtenir
  - Créer liste de contacts
  - Synchronisation automatique

## 📄 Upload CV

- [ ] Créer dossier `app/static/uploads/cv/`
- [ ] Upload du CV (PDF)
- [ ] Route de téléchargement fonctionnelle
- [ ] Versioning du CV (optionnel)

## 👨‍💼 Backoffice Admin

- [ ] Page de gestion des messages de contact
- [ ] Marquer comme lu/non lu
- [ ] Répondre directement depuis l'interface
- [ ] Filtres : recrutement, newsletter, date
- [ ] Statistiques des contacts

## ✅ Autres

- [ ] Tests du formulaire (pytest)
- [ ] Rate limiting (éviter spam)
- [ ] Logs des envois d'emails
- [ ] Notifications admin (nouveau contact)