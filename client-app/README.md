# Simulateur client

Simulateur de comportement des souris dans un labyrinthe

## Prérequis

1. Assurez-vous que `NodeJs 20` est installé sur votre machine 
2. Vous pouvez vérifier en utilisant la commande `node --version`
3. Ensuite, naviguez dans le dossier du projet, plus précisément dans le dossier  `client-app` via le terminal ou l'invite de commandes
4. Installez les dépendances en exécutant `npm install` ou `yarn install`
5. Renommez `.env.example` en `.env`

## JSON Mock Server (faculatif si les serveurs réels sont disponibles)

Au cas où l'API principale ne serait pas disponible ou prête, vous pouvez utiliser l'outil json-server pour tester l'application.

Suivez les étapes suivantes pour installer json-server :

1. Exécutez la commande `npm install -g json-server` dans votre terminal
2. Vérifiez que le port spécifié dans le fichier `json-server.json` n'est pas déjà utilisé
3. Enfin, lancez la commande `json-server --watch data/data.json --routes routes.json`

## Lancement de l'application en mode développement

Exécutez la commande suivante dans le terminal : `npm start`

Cliquez sur [http://localhost:3000](http://localhost:3000) pour l'afficher dans votre navigateur ou utiliser la version bureau.