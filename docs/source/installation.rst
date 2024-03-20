Instructions d'installation
=====

Prérequis
------------
* Compte GitHub avec accès en lecture au repository de l'application
* Git CLI
* SQLite3 CLI
* Interpréteur Python, version 3.6 ou supérieure
Dans le reste de la documentation sur le développement local, il est supposé que la commande python de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

macOS / Linux
------------
**Cloner le repository**

* cd /path-to-put-project-in
* git clone https://github.com/Mylaana/P13-DA-Python-PipelineCICD.git

**Créer l'environnement virtuel**

* cd /path-to-Project/app
* python -m venv venv
* apt-get install python3-venv (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
* Activer l'environnement source venv/bin/activate
* Confirmer que la commande python exécute l'interpréteur Python dans l'environnement virtuel which python
* Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure python --version
* Confirmer que la commande pip exécute l'exécutable pip dans l'environnement virtuel, which pip
* Pour désactiver l'environnement, deactivate

**Installer les dépendances**

* cd /path-to-Project
* source venv/bin/activate
* pip install --requirement requirements.txt
* deactivate

Windows
------------
Utilisation de PowerShell, comme ci-dessus sauf :

* Pour activer l'environnement virtuel, .\venv\Scripts\Activate.ps1
* Remplacer which <my-command> par (Get-Command <my-command>).Path
