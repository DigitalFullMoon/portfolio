02-PORTFOLIO/
│
├── app/                              # Ton application Flask
│   ├── __init__.py                  # Initialise Flask + extensions
│   ├── models.py                    # Modèles BDD
│   ├── forms.py                     # Formulaires généraux
│   ├── decorators.py                # Décorateurs personnalisés (vérif rôles)
│   ├── config.py                    # Config centralisée
│   │
│   ├── auth/                        # 🔐 Module authentification
│   │   ├── __init__.py
│   │   ├── routes.py               # Login, logout, register (avec reCAPTCHA)
│   │   └── forms.py                # Formulaires login/register
│   │
│   ├── main/                        # 🏠 Module public (frontend)
│   │   ├── __init__.py
│   │   ├── routes.py               # Homepage, portfolio, contact, newsletter
│   │   └── forms.py                # Formulaire contact + newsletter
│   │
│   ├── blog/                        # 📝 Module blog
│   │   ├── __init__.py
│   │   ├── routes.py               # Liste articles, détail, commentaires
│   │   └── forms.py                # Formulaire commentaire
│   │
│   ├── admin/                       # 👨‍💼 Module backoffice (Super Admin)
│   │   ├── __init__.py
│   │   ├── routes.py               # Dashboard, gestion contenu
│   │   ├── forms.py                # Formulaires CRUD articles
│   │   └── utils.py                # Helpers (upload, stats, etc.)
│   │
│   ├── api/                         # 🔌 Module API (Brevo, reCAPTCHA)
│   │   ├── __init__.py
│   │   ├── brevo.py                # Intégration Brevo
│   │   └── recaptcha.py            # Validation reCAPTCHA
│   │
│   ├── static/                      # Fichiers statiques
│   │   ├── css/
│   │   │   ├── main.css            # CSS général
│   │   │   ├── admin.css           # CSS backoffice
│   │   │   └── dark-mode.css       # Dark mode
│   │   ├── js/
│   │   │   ├── main.js             # JS général
│   │   │   ├── dark-mode.js        # Toggle dark mode
│   │   │   └── admin.js            # JS backoffice
│   │   ├── images/
│   │   │   ├── portfolio/          # Images projets
│   │   │   └── blog/               # Images articles blog
│   │   └── uploads/                 # Fichiers uploadés
│   │       ├── cv/                 # CV téléchargeables
│   │       └── blog_images/        # Images uploadées pour articles
│   │
│   └── templates/                   # Templates HTML
│       ├── base.html               # Template de base général
│       ├── base_admin.html         # Template de base backoffice
│       │
│       ├── auth/                   # 🔐 Templates authentification
│       │   ├── login.html
│       │   └── register.html       # Avec reCAPTCHA
│       │
│       ├── main/                   # 🏠 Templates frontend
│       │   ├── home.html
│       │   ├── portfolio.html
│       │   ├── contact.html        # Avec reCAPTCHA
│       │   └── newsletter_confirm.html  # Confirmation inscription
│       │
│       ├── blog/                   # 📝 Templates blog
│       │   ├── list.html           # Liste des articles
│       │   └── detail.html         # Détail + commentaires
│       │
│       ├── admin/                  # 👨‍💼 Templates backoffice
│       │   ├── dashboard.html      # Tableau de bord avec stats
│       │   ├── posts/
│       │   │   ├── list.html       # Gestion articles
│       │   │   ├── create.html     # Créer article (avec éditeur)
│       │   │   └── edit.html       # Éditer article
│       │   ├── comments/
│       │   │   └── moderation.html # Approuver/supprimer commentaires
│       │   ├── newsletter/
│       │   │   └── subscribers.html # Liste abonnés (sync Brevo)
│       │   └── users/
│       │       └── list.html       # Liste utilisateurs inscrits
│       │
│       ├── includes/               # Composants réutilisables
│       │   ├── navbar_home.html    # Navbar homepage
│       │   ├── navbar_pages.html   # Navbar autres pages
│       │   ├── navbar_admin.html   # Navbar backoffice
│       │   ├── footer.html         # Footer avec newsletter
│       │   └── flash_messages.html # Messages flash
│       │
│       └── errors/                 # Pages d'erreur
│           ├── 403.html            # Accès interdit
│           ├── 404.html            # Page non trouvée
│           └── 500.html            # Erreur serveur
│
├── docker/                          # Configuration Docker
│   └── mysql/
│       └── init.sql                # Script initialisation BDD
│
├── migrations/                      # Migrations BDD (Flask-Migrate)
│   └── versions/                   # Versions (auto-généré)
│
├── tests/                          # Tests (futur)
│   └── __init__.py
│
├── .env                            # Variables d'environnement (SECRETS!)
├── .env.example                    # Exemple sans secrets
├── .gitignore                      # Fichiers à ignorer
├── docker-compose.yml              # Orchestration containers
├── Dockerfile                      # Image Flask
├── requirements.txt                # Dépendances Python
├── config.py                       # Configuration Flask
└── run.py                          # Point d'entrée