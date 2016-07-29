# resilienceServer
Server with resilience metrics data.

## Installation

Assuming that you have python 3.4.X, pip3 and virtualenv, clone the repository. To install the required dependences:

```
$ virtualenv -p python3 venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ cd src
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py collectstatic
```

## Running

```
$ . venv/bin/activate
(venv) $ cd server
(venv) $ python manage.py runserver
```
