## Django Blog Project


A simple blog web application built with Django. It allows users to browse posts, search, filter by category and leave comments.
Admins can create, edit and publish blog posts with images.



## Features

 - Blog post list and detail pages
 - Categories and sidebar filter
 - search bar
 - Image uploads
 - comments system
 - Pagination
 - Admin interface
 - Base template with inheritance

 --


## Install and create a virtual environment:

 - pip install virtualenv
 - virtualenv venv

## Activate virtual environment:

 - source venv/bin/activate

## Deactivate virtual environment:
 - deactivate


## Install dependencies

 - pip install -r requirements.txt


## Apply migrations
 
 - python manage.py migrate


## Create superuser

 - python manage.py createsuperuser


### Run the development server

 - python manage.py runserver

 - Open http://127.0.0.1:8000 in your browser.