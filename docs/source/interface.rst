Interface de programmation
=====

Architecture
------------
Le programme est découpé en trois applications django distinctes :

* oc_lettings_site (url, settings).
* lettings (views et models liés aux Adresses et Lettings).
* profiles (views et models liés aux Profils).

Endpoints du site (URLs)
------------

* ``/`` Accueil du site.
* ``lettings/`` Liste des locations.
* ``lettings/<letting_id>/`` Détails de la location ``<letting_id>``.
* ``profiles/`` Liste des profils utilisateurs.
* ``profiles/<username>`` Détails concernant un utilisateur ``<username>``.
* ``admin/`` Page d'administration du site.