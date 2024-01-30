#!/bin/bash
cd /home/apps
source env/bin/activate
sudo pip install -r requirements.txt
deactivate