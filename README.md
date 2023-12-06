# INF756-TP
Ce repo est dédié au projet de fin de session du cours de Système Client Serveur (INF756).

## Contexte
L'Agence Spatiale Canadienne (ASC) pour la préparation de ses futures vols humains nous offre un contrat afin de pouvoir tester différents modèles de comportement et les différentes éventualités pendant les vols.
Pour cela, nous avons mis en en place des labyrinthes dans lesquels les souris peuvent évoluer.

## Prérequis
* [Docker](https://docs.docker.com/desktop/)
* [Node](https://nodejs.org/en/download)

## Installation
Après avoir installé les prérequis, exécuter la commande `docker compose up` dans le dossier
INF756-Project.
6 containers démarreront à la suite de l'exécution de cette commande;
* inf756-project_db
* pgadmin4_container
* inf756-project_redis
* inf756-project_intelligence
* inf756-project_simulation
* inf756-project_objects
Vérifié que les containeurs ont bien démarré.

Une fois fait veuillez aller dans le dossier INF756-Project/client-app et exécuter la commande `npm install` puis
`npm start`

Une fenêtre s'ouvrira et vous permettra d'utiliser l'application.
Vous pouvez aussi accéder à l'application en ouvrira un fureteur de votre choix et en allant à l'adresse http://localhost:3000

## Guide d'utilisation

Une fois que l'application est démarrée, vous aurez la possibilité de :

* Sélectionner le labyrinthe désiré pour la simulation. Il y en a 2 de disponibles. 
  * 1 labyrinthe de 5x5
  * 1 labyrinthe de 10x10

* Sélectionner le nombre de souris pour la simulation

* Sélectionner les règles de la simulation. Nous en avons 2 :
  * Une simulation facile qui contient :
    * Lorsqu’une souris fait 4 pas son état physique baisse de 1 point.
    * L'état physique et mental d'une souris augmentent de 3 points quand elle mange.
    * L'état physique d'une souris baisse de 2 points si elle tombe dans un petit piège.
    * L'état mental d'une souris baisse de 3 points si elle entre en collision avec un monstre.
    * L'état physique et mental d'une souris augmentent au maximum si elle boit une potion magique.
    * Lorsque la souris boit de l’alcool, tous ses attributs baisse de 3 points (intelligence, mental, santé).

  * Une simulation un peu plus difficile qui contient :
    * Lorsqu’une souris fait 4 pas son état physique baisse de 2 points.
    * L'état physique et mental d'une souris augmentent de 2 points quand elle mange.
    * L'état physique d'une souris baisse de 4 points si elle tombe dans un petit piège.
    * L'état mental d'une souris baisse de 5 points si elle entre en collision avec un monstre.
    * L'état physique et mental d'une souris augmentent au maximum si elle boit une potion magique.
    * Lorsque la souris boit de l’alcool, tous ses attributs baisse de 5 points (intelligence, mental, santé).

* Nous pourrons par la suite attribuer une intelligence aux souris sélectionner et lancer la simulation.

Une fois la simulation lancée, vous pourrez observer l’avancer des différentes souris.


