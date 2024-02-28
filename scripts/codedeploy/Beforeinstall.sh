#!/bin/bash

# removes all existing containers/images/volumes
sudo docker system prune -af
sudo docker volume prune -af