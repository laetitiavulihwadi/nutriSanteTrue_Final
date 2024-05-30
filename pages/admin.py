from django.contrib import admin

#import the models
from .models import *
# register each model with the admin site
admin.site.register(BlogPost)


# Register your models here.
admin.site.register(Recette)


# Register your models here.
admin.site.register(UserAgent)