#!/usr/bin/env bash

set -o errexit  # exit on error

apt-get install -y python3-tk 

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate