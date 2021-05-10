# Ce que fait le script:

    1- Choisir dans quel Bucket on fait la tâche. 
    2- Copier des fichiers locaux sur un compartimenrt Amazon S3.
    3- Supprimer des fichiers présent sur S3.
    4- télécharger des fichiers présent sur S3 vers le disque local.

# Ce script est composé de 4 mudules:

Qui sont applé dans la page principale,
    - Le mudule 1 app.py la page principale sert à  exécuté le programme qui contient les pages html, et les fonctions de copier, télécharger et supprimer.
    - Le mudule 2 resources.py qui contient les resources d'identification des client S3, et la fonction de la resource S3.
    - Le mudile 3 Filters.py sert à deduire le type de fichier, et afficher la date de la derniere modification.
    - Le mudule 4 config.py sert à stocker l'ID et le code secret du bucket.


# La manoeuvre de l'utiliser:

Ce script peut s'excuter sur nimporte quel environnement de développement (PowerShell, Vicual studio...) , il sufit de l'ouvrir et l'exécuter

# Réference de contact:

h.chaoui@systeme-reseaux.fr 
