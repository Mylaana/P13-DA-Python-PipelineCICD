#!/bin/bash

# remove directory and recreate it
cd /home/ubuntu
sudo rm -rf oc_lettings_site
mkdir oc_lettings site

# removes all existing containers/images/volumes
sudo docker system prune -af
sudo docker volume prune -af