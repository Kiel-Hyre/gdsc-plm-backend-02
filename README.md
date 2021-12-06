## About GDSC-PLM-BACKEND-02
- A series of activities provided to learn Django as a whole and as a backend

## Requirements
* [pip3](https://www.python.org/)
* [virtualenv](https://pypi.org/project/virtualenv/)
* [django](https://pypi.org/project/Django/)
* [postgresql](https://www.postgresql.org/)

## Setup
* Virtual Environment

1. Use virtualenv to add a virtual environment
```
    virtualenv venv
```
2. Activate the environment
```
    source venv/bin/activate  #Ubuntu
```
3. Deactivate enviroment
```
    deactivate
```
4. Remove environment
```
    rm -rf venv
```
Check this [info](https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/)
for windows


* Install requirements for python3
1. (Optional) Upgrade Tools
```
    pip3 install --upgrade setuptools #pip only for Windows
```
2. (Optional) Upgrade Pip
```
    python3 -m pip install --upgrade pip #python only for Windows unless there is other version
```
3. Install requirements in requirements.txt
```
    pip3 install -r requirements.txt
```

* Environment Variables
1. In source folder aligned with manage.py create **.env** file
```
    plmat-drf\
        ... # other files
        .env
        manage.py
```
2. Create variables inside env file
    1. For development, copy the variables inside the development.env to .env
    2. For production, copy the variables inside the production.env to .env

* Setup Postgresql
1. Follow the installation on this [guide](https://medium.com/@9cv9official/creating-a-django-web-application-with-a-postgresql-database-on-windows-c1eea38fe294)
2. By default
```
    server: localhost
    database: postgres
    port: 5432
    username: postgres
    password: <your password entered via installation>
```
3. Those keys will be used via .env DATABASE_URL, replace:
```
    DATABASE_URL = "postgresql://<yourusername>:<yourpassword>@<yourhost>:<yourport>/<yourdatabase>"

    e.g  DATABASE_URL = "postgresql://root:123@root:5432/test"
```

* Common Commands for Django

1. Makemigrations
```
    python3 manage.py makemigrations
```
2. Migrate Applications
```
    python3 manage.py migrate
```

## Run Servers

1. Run server for Django
```
    python3 manage.py runserver (port) # default is 8000
```

## GDSC-PLM-BACKEND-02

## BACKEND ACTIVITY 01

- Create a user api using simpleJWT

- Installation and plugin it was very easy just follow the quickstart provided by
simpleJWT [here](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)

- By default it will provide an access and refresh token

- An example of a successful response from access is:
```
    {
        refresh: #some hash
        access: # some hash
    }
```

- An example of a successful refresh is:
```
    {
        access: # some hash
    }
```

- Though it satisfy our common needs sometimes it best to override the output e.g inserting the user in the response
- Therefore we need to change some of the methods provided by the default
- By using python concepts and OOP concept we achieved it

- Therefore /token/ should provided like this
```
    {
        refresh: # some hash
        access: # some hash
        username : username
        email: email
    }
```
- And /token/refresh/ should output like /token/


- Some methods can also be made like /access/ wherein it just throw again the provided response
    Which common api when reloading a page with constant update versus storing it to a localstorage
- And /logout/ in which it revokes a token

- But its for you to explore :)

