# Django Basic project template
This is a simple and minimal Django app intended to be used as a point of departure in your django project adventure.
The [debug toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) has been added to the project in order to simplify your life while developing.


## Usage Instructions
Clone this repository e.g.
```
git clone https://github.com/pycodebe/django-basic.git
```

Navigate to the project
```
cd django-basic
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