# di data-hub django proof of concept

# How to start
The code already contains a database with some sample data. It's superuser is demo, password demo.

1) First of all (recommended but not mandatory) create a new virtualenv space
    to isolate django config from the rest of the system
    $ mkvirtualenv name_of_my_new_virtualenv

2) Install dependencies through pip
    $ pip install -r requirements.txt

3) cd into apps and run the app, using the desired address
    $ ./manage.py runserver 127.0.0.1:8000

4) Go to any of this URLs to check the API
    http://127.0.0.1:8000/api/spotlight/ # gets you list of current spotlightss

5) You can also check/modify the data in the admin panel:
   http://127.0.0.1:8000/admin

6) Incase you make changes to the models please run ./manage.py makemigrations
  and ./manage.py migrate for them to persist

# TOFIX / TODO
- create view for base URL
- Use nginx as reverse proxy server
