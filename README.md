# e-learning

e-learning test backend

Developed using:
- virtualenv with python 3.6.x
- Django==3.0.3
- Sqlite3 db for convenience

## Setup and Run
#### On an active env with python>=3.6:

1. Install requirements:
```console
$ pip install -r requirements.txt
```

2. Run migrations:
```console
$ python manage.py migrate
```

3. Start the development server:
```console
$ python manage.py runserver 
```

## WIP/todo

For ease of implementation and rapid prototyping, 
this first version omitted the following core features/Business Rules:

- The courses are correlative with previous ones
- The lessons are correlative with previous ones
- Auth strategy
