# Project Name
Newsweb Django REST Framework API

## Overview
This website is a simple newsweb site where users can register, create newsletters with email notification, and articles

## Requirements
- Docker
- Docker Compose
- Postman

## Installation and Setup
1. Clone the repository: git clone https://github.com/wolverkz/restAPI.git
2. Change directory: cd restAPI/newsweb/
3. Build and run the db container first: docker compose up -d db
4. Build and run the remaining containers: docker compose up -d
5. Run this command to get inside newsweb-web-1 container: docker exec -it newsweb-web-1 bash
6. Create superuser: python manage.py createsuperuser
7. Type your username, email, and password
8. Run this command to load data from fixture: python manage.py loaddata fixture.json
9. Exit the container by pressing CTRL + D

Now website is up and running.

## Usage
To open the website, type http://localhost:8000/. If you run the website on your VM, then instead of localhost, use the
IP address of your VM.

Now you can log in as admin and create newsletters and articles

To register new user, open the Postman and type this URL http://192.168.107.195:8000/register/ and send POST request.
Then choose Body, Raw, and JSON. After that, use the following template to add a new user.
{
    "username": "your_username",
    "email": "your_email",
    "password": "your_password"
}

If you want to delete a user, open the Postman and type this URL http://192.168.107.195:8000/users/ and send GET request.
You should see the list of users in the terminal bellow. Choose the user you want to delete by clickin on URL or
by typing this URL http://192.168.107.195:8000/users/user_pk/ (change the user_pk accordingly) and send DELETE request.

When you create a newsletter, an email will be sent to everyone who is registered and typed their correct email address.

## Troubleshooting
If you run "docker compose up -d" first, website will not open. Simply stop all the containers and run them again.
If you want to make changes inside the running container newsweb-web-1, you must type first "apt-get update" and then
"apt-get install nano". With nano, you can make changes inside the container. Example: nano docker-compose.yml

## Built With
* [Django](https://www.djangoproject.com/): Python web framework.
* [Django REST Framework](https://www.django-rest-framework.org/): Toolkit for building Web APIs in Django applications.
* [Celery](https://docs.celeryproject.org/): An asynchronous task queue/job queue based on distributed message passing.
* [RabbitMQ](https://www.rabbitmq.com/): A message broker that implements the Advanced Message Queuing Protocol (AMQP).
* [PostgreSQL](https://www.postgresql.org/): Open-source relational database management system.