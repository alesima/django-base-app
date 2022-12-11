Django Base App
============

`django-base-app` provides static files and base HTML laytout.

Instructions
------------

1. Add `django-base-app` to your INSTALLED_APPS setting like this:
   
   INSTALLED APPS = [
       ...,
       'django-base-app',
   ]

2. Include `urls.py` from `django-base-app` module in your `urls.py` like this:
  
   url(r'^api/', include('django_base_app.urls')),



 
