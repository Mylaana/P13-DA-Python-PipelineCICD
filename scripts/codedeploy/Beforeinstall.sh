#!/bin/bash

cd /home/ubuntu/oc_lettings_site
sudo docker-compose down
docker system prune -a
docker volume prune -a