## Installation 

Clone the repository

```
   git clone git@github.com:idahmed/paytic_test.git
```

Navigate to the project directory

```
  cd your-django-app
```

Change MONGO_URI in setting to your db URI 

Install Pipenv if not already installed
```
  pip install pipenv
```

Install project dependencies using Pipenv
```
  pipenv install
```

Activate the virtual environment
```
  pipenv shell
```

Perform initial database migrations
```
  python manage.py migrate
```
