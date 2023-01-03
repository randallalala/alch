$ python3 manage.py startapp cocktails    
$ python3 manage.py makemigrations      # for updating models too 
$ python3 manage.py migrate
$ python3 manage.py shell 
$ python3 manage.py startapp users    # for user login app that can be resused
$ pip install django-crispy-forms

% ADD APPS  
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    
    "cocktails",
    "users",]


% links
- /admin #to go into admin section