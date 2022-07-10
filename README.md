# Tortoise sample application

## Setup (without docker)

The first thing to do is to clone the repository:

```bash
$ git clone https://github.com/kush225/assignment
$ cd tortoise
```

Create a virtual environment to install dependencies in and activate it:

```bash
$ python -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```bash
(env)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```bash
(env)$ python manage.py runserver
```
And navigate to [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

## Setup (with docker)
Create docker image
```
docker build -t tortoiseapp .
```
Run docker image
```
docker run -it -p 8000:8000 tortoiseapp:latest
```
And navigate to [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)


## Brand Partner Side

### Actions:
1. Signup
2. Create brand
3. Create plan/list brand user plans.
4. Create promotion/list promotions available in plan.
5. List customer goals

### Flow:
1. Create a new user or use existing user.
```
username: user1
password: pass@123 
```
2. Create brand -> plan -> promotion.


## End User side.

### Actions:
1. Signup
2. List available plans on the platform or brand
3. Create customer goals

### Flow:
1. Create a new user or use existing user.
```
username: user2
password: pass@123
```
2. Create customer goal
