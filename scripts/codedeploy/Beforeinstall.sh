#!/bin/bash

# removes all existing containers/images/volumes
docker system prune -a
docker volume prune -a