# Simulateur client

Simulateur de vol piloté par une IA

## Prérequis

1. Installez les dépendances en exécutant `npm install` ou `yarn install`
2. Renommez `.env.example` en `.env` et renseignez `REACT_APP_API_BASE_URL`

## JSON Server

Au cas où l'API principale ne serait pas disponible ou prête, vous pouvez utiliser l'outil json-server pour tester l'application.

Suivez les étapes suivantes pour installer json-server :

1. Exécutez la commande `npm install -g json-server` dans votre terminal
2. Vérifiez que le port spécifié dans le fichier `json-server.json` n'est pas déjà utilisé
3. Enfin, lancez la commande `json-server --watch data/data.json --routes routes.json`

## Lancement de l'application en mode développement

Exécutez la commande suivante dans le terminal : `npm start`

Cliquez sur [http://localhost:3000](http://localhost:3000) pour l'afficher dans votre navigateur.