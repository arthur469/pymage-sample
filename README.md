# Pymage Downloader

Pymage Downloader est un outil simple et efficace pour télécharger des images aléatoires depuis [Lorem Picsum](https://picsum.photos/). Il propose une interface graphique et une interface en ligne de commande.

## Fonctionnalités

- Téléchargement asynchrone d'images
- Interface graphique conviviale
- Support de la ligne de commande
- Dimensions d'images personnalisables
- Option de dimensions aléatoires
- Journalisation des opérations

## Prérequis

Pour installer les dépendances nécessaires :

    pip install -r requirements.txt

## Utilisation

### Interface Graphique

Lancez simplement le script sans arguments :

    python main.py

### Ligne de Commande

    python main.py --sizes "4@800x800,2@1920x1080,3@random"

### Format des Spécifications

Les dimensions sont spécifiées au format suivant :
- `nombre@largeurxhauteur` : Pour des dimensions fixes
- `nombre@random` : Pour des dimensions aléatoires

Exemples :
- `4@800x800` : 4 images de 800x800 pixels
- `2@1920x1080` : 2 images en Full HD
- `3@random` : 3 images avec des dimensions aléatoires

## Structure du Projet

    pymage-downloader/
    │
    ├── main.py           # Script principal
    ├── downloaded_images/ # Dossier des images téléchargées
    └── README.md         # Documentation

## Journalisation

Le programme enregistre toutes les opérations dans la console avec les informations suivantes :
- Création du dossier de téléchargement
- Statut des téléchargements
- Erreurs éventuelles

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

## Licence

Ce projet est sous licence MIT.
