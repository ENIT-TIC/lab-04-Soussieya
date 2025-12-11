Docker + Flask + SQLite : Books API
Objectif du TP

Ce TP a pour but de créer une API RESTful pour gérer une bibliothèque de livres en utilisant Flask et SQLite, le tout conteneurisé avec Docker. L’objectif est de pratiquer :

Le développement d’une API avec Flask.

La manipulation de bases de données SQLite.

La création et la gestion de conteneurs Docker.

La persistance des données avec Docker volumes.

Prérequis

Docker et Docker Compose installés sur votre machine.

PowerShell ou terminal pour tester les endpoints.

(Optionnel) curl pour tester les requêtes HTTP.

Structure du projet
lab-03aa-Soussieya-main/
│
├─ app.py                # API Flask
├─ books.db              # Base SQLite (initialement vide)
├─ Dockerfile            # Conteneur pour l’API
├─ docker-compose.yaml   # Définition des services Docker
├─ requirements.txt      # Librairies Python nécessaires
├─ db-test.py            # Script de test de connexion à la DB
└─ README.md             # Ce fichier

Étapes réalisées
1. Création de l’API Flask

app.py initialise la base de données SQLite si elle n’existe pas.

Routes créées :

GET /books → Liste tous les livres.

POST /books → Ajoute un livre.

GET /books/<id> → Récupère un livre par son id.

PUT /books/<id> → Met à jour un livre.

DELETE /books/<id> → Supprime un livre.

2. Conteneurisation avec Docker

Création du Dockerfile pour l’API Flask.

Exposition du port 5000.

Installation des dépendances via requirements.txt.

3. Docker Compose

Création du docker-compose.yaml pour lancer le conteneur API.

Utilisation d’un volume Docker pour persister la base SQLite (./data:/app/data).

4. Lancement des conteneurs
docker-compose up --build


Vérification avec docker ps pour s’assurer que le conteneur est actif.

L’API est accessible sur : http://127.0.0.1:5000

5. Test des endpoints

GET /books (liste des livres) :

Invoke-RestMethod -Uri http://localhost:5000/books -----> voir GetBooks.png  et GetBooks1.png 


POST /books (ajout d’un livre) :

Invoke-RestMethod -Uri http://localhost:5000/books -Method POST -Body (@{
    title = "Docker avec SQLite"
    author = "Eya Soussi"
    year = 2025
} | ConvertTo-Json) -ContentType "application/json"

----------> voir PostBooks.png


Résultat attendu :

GET renvoie la liste des livres avec le nouveau livre ajouté. ---------> voir list_books.png

Les modifications sont persistées grâce au volume Docker.

6. Arrêt et nettoyage
docker-compose down


Supprime les conteneurs et le réseau créé par Docker Compose.

Les données restent persistées dans le volume Docker.

7. Test des endpoints

GET /books

Invoke-RestMethod -Uri http://localhost:5000/books


POST /books

Invoke-RestMethod -Uri http://localhost:5000/books -Method POST -Body (@{
    title = "Docker avec SQLite"
    author = "Eya Soussi"
    year = 2025
} | ConvertTo-Json) -ContentType "application/json"