#!/bin/bash
cd /home/apps
source env/bin/activate
pip install -r requirements.txt
deactivate

#printing instance dns in file
result=$( aws ec2 describe-instances --instance-ids i-04addbebb4c86a95e --query 'Reservations[].Instances[].PublicDnsName' | sed 's/[\["\]//g; s/]$//' | tr -d '\n' | sed 's/^[ \t]*//;s/[ \t]*$//')
sudo sed -i 's/ec2_dns/'"${result}"'/g' setup.cfg