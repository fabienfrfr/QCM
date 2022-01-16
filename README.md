# QCM

###### Attribution required : Fabien Furfaro (CC 4.0 BY NC ND SA)
---


Steps :
* Extract text of imageQCM with tesseract-ocr
* Extract QCM in HTML to CSV (or SQL) : Beautiful soup

In ubuntu, don't forget to add an "files.txt" in /template folder, if you want to add any text file in any folder with right-click.

Django (https://docs.djangoproject.com/fr/4.0/intro/tutorial01/) :
In parent directory (if not created) : django-admin startproject QCM_WEBSITE
Run the server (in the goot repertory) : python3 manage.py runserver
Go in web browser : http://127.0.0.1:8000/
Create an app (named polls) : python manage.py startapp polls
modify views and add urls in poll and qcm for pointer
Go in web browser : http://127.0.0.1:8000/polls
create database table : python3 manage.py migrate
