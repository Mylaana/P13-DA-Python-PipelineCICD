## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiment - Fonctionnemment du pipeline Ci/Cd
Le pipeline est concu pour que le(s) développeur(s) travaille(nt) sur des branches de features/bug qui sont ensuite merge vers la branche development.

### Intégration continue
Lors d'un push sur une branche du repository Github, le code est compilé et testé via Pytest, les erreurs de linting détectés via Flake8.
Si le push était sur la branche "development" :
- Si les tests sont OK, une pull-request est crée automatiquement et merge vers la branche main.
- Le workflow génere ensuite une image docker et la teste, puis la push sur le repository Docker.io.

### Déploiement continu
Une fois le code intégré à la branche main, le service AWS Pipeline détecte les changements de code source et active le service CodeDeploy :
- Arrete l'application, ses conteneurs, et supprime l'ancien code source de l'instance EC2
- Copie le code source et le déploi sur l'instance
- Crée deux conteneurs et un volume via docker compose (Nginx, Gunicorn+Application)
- Démarre les conteneurs et remet le site web en ligne

## Déploiement - Mise en place du pipeline Ci/Cd
### Prérequis
- Compte GitHub
- Compte Docker Hub
- Compte AWS
- Compte Sentry

### Docker
-  Rendez-vous sur le site docker.io.
-  Téléchargez et installez l'application Docker Desktop.
-  Connectez votre compte à l'application.
-  Allez dans l'interface de docker.io, dans les parametres de sécurité du compte créez un Token d'acces avec les droits de lecture/ecriture.

### Github
- Rendez-vous sur le site de GitHub et connectez-vous à l'interface.
- Allez sur le repository dans les settings section secrets/actions
- Ajoutez les Tokens de docker.io DOCKER_TOKEN, DOCKER_USERNAME liés au compte docker

### Sentry
- Rendez-vous sur le site de sentry
- Créez un nouveau projet Django
- Récupérez la clé dsn et copiez la dans le fichier .env, à la racine de l'application, ligne DSN

### AWS
- Rendez-vous sur le site d'AWS, connectez-vous à l'interface via un IAM administrateur (ou compte root).
- Déployez une instance EC2 utilisant l'OS Ubuntu.
- Dans le service IAM, créez un role autorisant l'utilisation du service CodeDeploy et attribuez le à l'instance (IAM Role de l'instance).
- Connectez-vous en SSH à l'instance et installez le CodeDeploy agent, docker et demarrez leurs services.
- Dans l'interface AWS, assurez vous que les regles de sécurité de l'instance autorisent les connexions entrantes au port 80 en protocole TCP.
- Rendez-vous ensuite dans le service CodeDeploy et créez une application.
- Dans la section Pipeline créez ensuite un Pipeline qui utilise l'application précédemment crée, connectez le compte Github lié au remote repository et ajoutez un trigger du pipeline lors d'un push sur la branche main.


### Fin
Le pipeline est maintenant fonctionnel !

