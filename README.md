#data hub proof of concept django backend for cms

# How to start
The code already contains a database with some sample data. It's superuser is demo, password demo.

1) First of all (recommended but not mandatory) create a new virtualenv space to isolate django config from the rest of the system
    $ mkvirtualenv name_of_my_new_virtualenv

2) Install dependencies through pip
    $ pip install -r requirements.txt

3) Run the sample code, use the desired address
    $ ./manage.py runserver 127.0.0.1:8000

4) Go to any of this URLs to check the API
    http://127.0.0.1:8000/api/spotlight/
    http://127.0.0.1:8000/api/indicators/

5) You can also check/modify the data in the admin panel:
   http://127.0.0.1:8000/admin

6) Play with the code and... enjoY!!
