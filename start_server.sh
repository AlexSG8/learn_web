#!/bin/bash
source .env/bin/activate
echo 'source changing'
export FLASK_APP=webapp
export FLASK_ENV=development
#export FLASK_ENV=
echo 'env variables exported'
flask run

