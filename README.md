# e-learning

e-learning test backend

Developed using:
- virtualenv with python 3.6.x
- Django 3.0.3
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

3. Create test user:
```console
$ python setup_users.py
```

4. Start the development server:
```console
$ python manage.py runserver 
```


## API

- Getting an auth token: 
```
POST /courses-api/token-auth/
  with params:
    - username = prof
    - password = pass
    
  Example return:
    { "token": "0b53f36ae04196d164c319ac61a224d4a9d3b16f" }
```

Now for each request use the header:
```
Authorization: Token 0b53f36ae04196d164c319ac61a224d4a9d3b16f
```
Note the work Token added before the token

#### Main Services
```
GET /courses/
GET /lessons/?course={course_id}
GET /questions/?lesson={lesson_id}
POST /take-lesson/?lesson={lesson_id}
    no params received, TODO -> receive answers
```


#### CRUD for main entities
Course, Lessons and Questions objects are RESTful

- Course:
```
/courses-api/courses/ 
  GET to retrieve the list of courses
  POST with params: name, course, approval_score
 
/courses-api/courses/{course_id}/
  GET
  PUT with params: name, course, approval_score
  DELETE
```

- Lessons and Questions
``` 
Same as Course but with the following base endpoint:
/courses-api/lessons/ 
/courses-api/questions/ 
```
