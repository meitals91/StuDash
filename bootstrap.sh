#!/bin/bash -ex

# Install Pipenv
sudo -n dnf install -y pipenv
cd /vagrant

# Install dependencies using Pipenv
pipenv sync

# Run Django app - remove comment when handling the Django task
# nohup pipenv run python manage.py runserver 0.0.0.0:8000 &