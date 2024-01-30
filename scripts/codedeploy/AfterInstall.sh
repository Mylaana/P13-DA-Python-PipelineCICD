#!/bin/bash
cd /home/apps
source env/bin/activate
pip install -r requirements.txt
deactivate

#printing instance dns in file
result=$( aws ec2 describe-instances --instance-ids i-04addbebb4c86a95e --query 'Reservations[].Instances[].PublicDnsName' | sed 's/[\["\]//g; s/]$//')
echo ALLOWED_HOST = $result > test_log.txt