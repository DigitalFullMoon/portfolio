# Dans VSC, ouvre le terminal intégré (Ctrl + `)

# 1. Vérifier que tu es bien connecté au repo
git remote -v

# 2. Créer une branche de développement (bonne pratique)
git checkout -b develop

# 3. Après chaque étape, commit
git add .
git commit -m "feat: configuration Docker initiale"

# 4. Push vers GitHub
git push origin develop

# 5. Quand une fonctionnalité est stable, merge dans main
git checkout main
git merge develop
git push origin main