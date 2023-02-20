$ python3 manage.py startapp cocktails    
$ python3 manage.py makemigrations      # for updating models too 
$ python3 manage.py migrate
$ python3 manage.py shell 
$ python3 manage.py startapp users    # for user login app that can be resused
$ pip install django-crispy-forms
$ python3 manage.py createsuperuser     # randallala pn19
$ pip install django-mathfilters (cocktail-detail.html)
$ pip install -r requirements.txt       # after activating venv
$ python3 manage.py test     
$ python3 manage.py test cocktails      # only test cocktail model

% ADD APPS  
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    
    "cocktails",
    "users",]


% links
- /admin #to go into admin section

features / done / learnt
- users and auth
- many to many (ingre / alch / uom)
- tests
- searches
- slugify
