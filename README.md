# TinyUrl

A flask based url shortener app. It uses random string generator to create the
short url.

## Instructions
### Install the requirements
`pip install -r requirements.txt`
It uses redis / postgres. 
### Configure
set environement vairable for DATABASE_URL and SECRET_KEY or edit the config.py
file.
`export FLASK_APP=run.py`

### Run migration
`flask db init`
`flask db migrate`
`flask db upgrade`

### Run 
`flask run`

