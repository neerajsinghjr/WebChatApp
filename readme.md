# Getting Started Guide
A guide to creating a new django project that uses:

### windows
### python3.8.2
### pip
### django 2.2.15 (LTS)
### virtualenv
### Redis
### django channels 2
### Postgres

## Install Python3.8.2
Bottom of page: https://www.python.org/downloads/release/python-382/


## Installing pip
https://pypi.org/project/pip/

- Open cmd prompt
- pip install pip
- Setup virtualenv
- Navigate to where you want to keep your django projects. I use D://DjangoProjects/
- Create D://DjangoProjects/ChatServerPlayground folder or whatever you want to name the project.
- Create a virtual environment to run the project in.
    Typically I call it "venv" but you can call it something else if you like. Doesn't matter. djangoproject_venv for example.
- python -m venv venv or python -m venv djangoproject_venv if you like
- Open a cmd prompt in your project directly
- Navigate into venv folder
- cd venv
- Activate the virtual environment
    Windows: Scripts\activate
    Linux: source bin/activate
    Mac (I think): source bin/activate

### Install Django and create Django project
- python -m pip install Django==2.2.15
See LTS: https://www.djangoproject.com/download/

### Create the django project
- django-admin startproject ChatServerPlayground
- Rename root directory (ChatServerPlayground) to src
    I prefer to name my root directory src because inside the project is another folder named ChatServerPlayground or whatever you called your project
    So now you should have the following folder structure:
    D://DjangoProjects/ChatServerPlayground/venv/src/
    Inside src you will have a folder name ChatServerPlayground and a manage.py file

### Keep track of the libraries you use
- pip freeze > requirements.txt
Run the server to make sure it's working
python manage.py runserver
Visit http://127.0.0.1:8000/

### Postgres Setup (Windows)
Postgres needs to run as a service on your machine. Since I'm using windows I will show you how to do this on windows. When we launch this website in production at the end of the course I'll show you how to setup postgres on Linux.

Download postgres: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

I am using x86-64 version 10 for windows
run the .exe file and go through the installation

### Remember the superuser password you use. This is very important.
- port 5432 is the standard

After installation confirm the service is running by opening the "Services" window on windows.
If it's not running then start it.
Confirm you have access to database
- open cmd prompt
- write psql postgres postgres

means: "connect to the database named 'postgres' with the user 'postgres'". 'postgres' is the default root user name for the database.
Some commands you'll find useful:
- List databases
\l
Connect to a different database
\c codingwithmitch_chat
Keep in mind you will not have any other databases. We will create one in a second.
List the tables in a database \dt
create a new database for our project
CREATE DATABASE codingwithmitch_chat_dev;
Create a new user that has permissions to use that database
CREATE USER django WITH PASSWORD 'password';
These credentials are important to remember because they are used in the django postgres configuration.
List all users
/du
Give the new user all privileges on new db
GRANT ALL PRIVILEGES ON DATABASE codingwithmitch_chat_dev TO django;
Test
disconnect from db
\q
Connect to the db with user
psql codingwithmitch_chat_dev django
Django and Postgres Setup
Install psycopg2
pip install psycopg2
Add to requirements
pip freeze > requirements.txt
Update settings.py with the following postgres configuration
DB_NAME = "codingwithmitch_chat_dev"
DB_USER = "django"
DB_PASSWORD = "password"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Delete the sqlite database in project root
migrate to commit changes to database
python manage.py migrate
create a superuser
python manage.py createsuperuser
log into admin
python manage.py runserver
visit http://127.0.0.1:8000/admin
This confirms the database is working correctly.
Install Redis (Required to send payloads to multiple clients at once)
Redis does not work "out of the box" on windows. There is a number of ways to get it working but by far the easiest is to use Menurai.

Links:
download: https://www.memurai.com/get-memurai
docs: https://docs.memurai.com/en/installation.html
Just download the executable and run it.
Update settings with CHANNEL_LAYERS configuration in settings.py
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}