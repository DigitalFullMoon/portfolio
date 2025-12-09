User
├── id
├── username
├── email
├── password (hashé avec bcrypt)
├── role (visitor / admin)
├── is_active
├── date_created
└── last_login

Post
├── id
├── title
├── slug (URL-friendly)
├── content (HTML de l'éditeur)
├── excerpt (résumé court)
├── author_id (FK → User)
├── featured_image
├── published (bool)
├── date_created
└── date_modified

Comment
├── id
├── content
├── author_id (FK → User)
├── post_id (FK → Post)
├── approved (bool - par défaut False)
├── date_created
└── date_moderated

Project
├── id
├── title
├── description
├── image_url
├── github_url
├── demo_url
├── technologies (JSON ou table séparée)
└── order (pour trier l'affichage)

Newsletter
├── id
├── email
├── brevo_contact_id (ID du contact chez Brevo)
├── is_active
├── date_subscribed
└── date_unsubscribed