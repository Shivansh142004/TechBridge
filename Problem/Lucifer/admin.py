from django.contrib import admin
from .models import Tweet



admin.site.register(Tweet) #Registering the tweet model with the admin site so that it can be checked and managed through the django admin interface.
# This allows the admin to view, add, edit, and delete tweets from the admin panel.

# Register your models here.
