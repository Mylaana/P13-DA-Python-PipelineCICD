#!/bin/bash

# remove directory content
cd /home/ubuntu/oc_lettings_site
sudo rm * -rf

# removes all existing containers/images/volumes
#sudo docker system prune -af
#sudo docker volume prune -af
