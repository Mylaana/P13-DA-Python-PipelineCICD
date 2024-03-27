Procédures de déploiement & gestion de l'application
=====

Le déploiement est assuré par un pipeline Ci/Cd. 
C'est un processus visant à automatiser les taches d'intégration du code suite à un commit, puis le déploiement des mises à jour en production (sur les serveurs cloud).

Intégration continue
------------
**Lors d'un commit sur la branche development du repository Github:**

* Reproduction de l'environnement de développement local (installation des dépendances et création d'un environnement virtuel).
* Vérification du formatage du code (Linting) via Flake8.
* Exécution de la suite de tests automatisés via Pytest, génération d'un rapport de couverture du code.

**Si le code est valide et sans erreur de formatage:**

* Création d'une image via Docker et lancement d'un conteneur.
* Push de l'image sur Docker hub.
* Création d'une pull request et automerge dans la branche main

L'ensemble de la CI est piloté par les GitHub Actions.
*Egalement, lors d'un commit sur n'importe quelle branche du repository, la CI lancera les tests et le linting du code (mais pas la pull-equest et la CD).

Déploiement continu
------------
**Lors d'une mise à jour du code source sur la branche main du repository GitHub:**

* Activation du service AWS Pipeline via webhooks (détection de changement dans la base de code sur le repository GitHub).
* Clone du repository GitHub et Activation du service AWS CodeDeploy.
* Arret des deux conteneurs dockers (1-Nginx 2-Gunicorn/Oc_Lettings).
* Suppression de la base de code sur l'instance EC2.
* Installation du code source mis à jour sur l'instance.
* Création des images et lancement des conteneurs via docker-compose.

Configuration de l'application
------------

Suivez ces étapes afin de configurer le déploiement:

**Pré-requis:**

* Compte GitHub
* Compte Docker Hub
* Compte AWS
* Compte Sentry

**Conteneurisation - Docker :**

*  Rendez-vous sur le site docker.io.
*  Téléchargez et installez l'application Docker Desktop.
*  Connectez votre compte à l'application.
*  Allez dans l'interface de docker.io, dans les parametres de sécurité du compte créez un Token d'acces avec les droits de lecture/ecriture.

**Github :**

* Rendez-vous sur le site de GitHub et connectez-vous à l'interface.
* Allez sur le repository dans les settings section secrets/actions
* Ajoutez les Tokens de docker.io DOCKER_TOKEN, DOCKER_USERNAME liés au compte docker

**Sentry :**

* Rendez-vous sur le site de sentry
* Créez un nouveau projet Django
* Récupérez la clé dsn et copiez la dans le fichier .env, à la racine de l'application, ligne DSN

**AWS :**

* Rendez-vous sur le site d'AWS, connectez-vous à l'interface via un IAM administrateur (ou compte root).
* Déployez une instance EC2 utilisant l'OS Ubuntu puis démarrez-la.
* Dans le service IAM, créez un role autorisant l'utilisation du service CodeDeploy et attribuez le à l'instance (IAM Role de l'instance).
* Connectez-vous en SSH à l'instance et installez le CodeDeploy agent, docker et demarrez leurs services.
* Dans l'interface AWS, assurez vous que les regles de sécurité de l'instance autorisent les connexions entrantes au port 80 en protocole TCP.
* Rendez-vous ensuite dans le service CodeDeploy et créez une application.
* Dans la section Pipeline créez ensuite un Pipeline qui utilise l'application précédemment crée, connectez le compte Github lié au remote repository et ajoutez un trigger du pipeline lors d'un push sur la branche main.


**Reverse proxy - Nginx :**

Le service des fichiers statiques de l'application est assuré par Nginx qui sert de reverse proxy, sa configuration se trouve dans le répertoire /proxy à la racine du projet.
Nginx est conteneurisé seul et utilisera un **volume** pour accéder aux fichiers statiques.

Nginx écoutera les requêtes reçues par l'instance EC2 sur le port 80 et dialoguera avec le conteneur de Gunicorn-Django afin qu'elles soient interprétées.

Afin d'améliorer la sécurité, ce conteneur est exécuté en tant que user "Nginx" non "Root".

**Web service - Gunicorn :**

L'application web est servie par Gunicorn qui assurera le traitement des requêtes sur les différents endpoints en production.
Gunicorn et l'application sont conteneurisés ensembles dans un deuxieme conteneur.
Afin d'améliorer la sécurité du site web, ce conteneur est exécuté en tant que user "User" non "Root"


**Test du pipeline Ci/Cd**

Pour tester le pipeline complet, il suffit de réaliser un commit sur la branche development.


Gestion de l'application
------------

**Administration du site**

Pour administrer l'application rendez-vous sur le lien :

``http://<lien-de-l'hébergeur>/admin/``

Connectez-vous à l'aide informations suivantes :

Login : ``admin``
Mot de passe : ``Abc1234!``

**Administration des objets :**

Une fois connecté sur l'interface d'administration, sélectionnez le modèle que vous souhaitez administrer.

Vous pouvez lire, ajouter, modifier et supprimer les entrées de ce modèle dans la base de données via les formulaires de l'interface admin.

**Journalisation des erreurs**

La journalisation (tracking & log) des erreurs est assurée par sentry, vous pouvez les consulter sur l'interface de sentry.io en vous connectant avec le compte lié à l'application.

**Base de données**

Les données sont actuellement stockées via SQLite qui convient parfaitement pour le moment mais nécessitera un changement de technologie ultérieur afin d'améliorer la scalabilité du site.
