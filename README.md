# Django Basic project template
This is a simple and minimal Django app intended to be used as a point of departure in your django project adventure.
* [debug toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) has been added to the project in order to simplify your life while developing.
* [whiteNoise](http://whitenoise.evans.io/en/stable/) will serve our static files
* [gunicorn](https://gunicorn.org/) is used as our WSGI HTTP server for production
* [nginx](https://hub.docker.com/_/nginx) is used as our reverse-proxy
* [docker & docker-compose](https://docs.docker.com/compose/) is used to run our django project and nginx server in containers


## Usage Instructions
Clone this repository e.g.
```
git clone https://github.com/pycodebe/django-basic.git
```

Navigate to the project
```
cd django-basic
```

Create and activate the environment
```
conda env create --file ./requirements.yml
conda activate venv
```

Run migrations to create the default database and create the model 'Hero'
```
python manage.py migrate
```

Run the Django development server
```
python manage.py runserver 0.0.0.0:8000
```

Navigate to to http://127.0.0.1:8000

## Environment variables
Create an .env file and and store it in app/ next to the /settings folder.
It should contain:
```
SECRET_KEY=<your secret key>
INTERNAL_IPS=<your IP for the debug toolbar>
```
