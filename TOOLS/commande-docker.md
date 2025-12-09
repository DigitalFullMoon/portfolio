# Arrêter les containers (Ctrl+C dans le terminal)
# Puis :
docker-compose down

# Relancer les containers
docker-compose up

# Relancer en arrière-plan (mode détaché)
docker-compose up -d

# Voir les logs en temps réel
docker-compose logs -f

# Voir seulement les logs de Flask
docker-compose logs -f web

# Rentrer dans le container Flask (comme SSH)
docker exec -it portfolio_flask bash

# Supprimer TOUT (containers + volumes) - ATTENTION données perdues !
docker-compose down -v