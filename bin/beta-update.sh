#!/bin/bash

beta_directory = '/home/james/OSD-beta/OSD'
backup_directory = /home/james/backups/OSD-beta-upgrade
current_date = date +%Y%m%d%H%M%S

# Stop the server
sudo systemctl gunicorn stop

# Backup the existing database
python ${beta_directory}/manage.py dumpdata --natural-primary > ${backup_directory}/${current_data}.json

# pull the database

sudo git pull

# check that the pull worked properly

if [ $? -ne 1 ]
then

    sudo git shelve
    sudo git pull
    sudo git shelve apply

else
    echo Pull complete

fi

