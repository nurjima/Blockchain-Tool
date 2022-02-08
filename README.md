# Blockchain Analytics Tool using Django framework

Following repository provides code that:

- Visualize top 100 Ethereum addresses by ETH Balance
- Displays in the browser 3 types of charts: Pie Chart, Bar Chart and Linear Chart
- Uses database PostgtreSQL to store addresses and their balance
______________________________________________________________________________________________

Assignment 2 was done in team - Shaliyeva N. SE-2012, Shamshidin S. SE-2008


## Installation
#### django
```
$ pip install pyjwt
```

#### requests
```
$ pip install requests
```

#### beautifulSoup
```
$ pip install beautifulsoup4
```
#### psycopg. It's necessary to install for connection with PostgreSQL DB
```
$ pip install psycopg2
```
***Note:** If it is not working try this:*
```
$ pip install psycopg2-binary
```


***Note:** If you are a MAC/Linux User type **3**, after keywords - pip and python*

## Usage
Install packages, that was mentioned before. Connect with database.
If you are PostgrteSQL user -> change info in settings.py in project folder. 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<name_of_database>',
        'USER': '<username>',
        'PASSWORD': '<your_password>',
        'HOST': '<host>',
        'PORT': '<port>',
    }
}
```
In case, you use databases like SQLite etc., check the django documentation - https://docs.djangoproject.com/en/4.0/

After typing your info into _setting.py_, you will need to do migrations by running this command in terminal/command prompt
```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

Then run the server:

### MacOS
```
python manage.py runserver
```

### Windows
```
python manage.py runserver
```
