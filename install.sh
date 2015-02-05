#!/bin/bash
mkdir bsuire_exo_census
cd bsuire_exo_census
virtualenv venv
cd venv
source bin/activate
pip install Django
git clone https://github.com/bsuire/dtk_census
cd dtk_census/census
mkdir db
cp ../../../../us-census.db  db/us-census.db
python manage.py inspectdb > base_stats/models.py
python manage.py runserver
