from django.db import models
from django.contrib.auth.models import Group, Permission
import os
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from nutri_sante.middleware import get_current_request

User = get_user_model()

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join("uploads/", filename)

# def filepath(instance, filename):
#     time_now = datetime.now().strftime('%Y%m%d%H%M%S')
#     filename, file_extension = os.path.splitext(filename)
#     new_filename = f"{time_now}_{filename}{file_extension}"
#     return os.path.join('uploads/', new_filename)

def validate_name(value):
    if not isinstance(value, str):
        raise ValidationError("Name must be a string.")

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only aphanumeric characters are allowed.')

# class Recette(models.Model):
#     permissions = [
#             ("publish_recette", "Can publish a recipe")
#         ]
#     id = models.AutoField(primary_key=True)
#     nom = models.CharField(max_length=100, validators=[validate_name,alphanumeric])
#     description = models.TextField(validators=[alphanumeric])
#     photo = models.ImageField(upload_to="recipes_images", null=True, blank=True)
#     creation_date = models.DateTimeField(auto_now_add=True)
#     user_crea = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nom
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         request = get_current_request()
#         if request:
#             messages.success(request, 'Recipe added successfully.')
#             print("SAVING RECIPE")

# ------------------------ Recepi updated
from django.contrib import messages
# from django.shortcuts import get_current_request

class Recette(models.Model):
    permissions = [
            ("publish_recette", "Can publish a recipe")
        ]
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, validators=[validate_name,alphanumeric])
    description = models.TextField()
    photo = models.ImageField(upload_to="recipes_images", null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    user_crea = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    def save(self, *args, **kwargs):
        # Save the Recette instance
        super().save(*args, **kwargs)

        # Get the current request object
        request = get_current_request()

        # Check if the request object is available
        if request is not None:
            # Add a success message to the request
            messages.success(request, 'Recipe added successfully.')
            print("SAVING RECIPE")

class BlogPost(models.Model):
    title = models.CharField(unique=True, max_length=100)
    content = models.TextField(blank=True)
    num_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    pub_date = models.DateField(null=True, blank=True)
    
    
def __str__(self):
    return self.title




class UserAgent(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nom
    

#  Group setup

# To create a group:from django.contrib.auth.models import Group, Permission

# Créer les groupes
nutritionist = Group(name='nutritionist')
# nutritionist.save()

chef = Group(name='chef')
# chef.save()

# Ajouter les permissions aux groupes
'''chef.permissions.add(Permission.objects.get(codename='view_recette'))

nutritionist.permissions.add(
    Permission.objects.get(codename='view_recette'),
    Permission.objects.get(codename='change_recette'),
    Permission.objects.get(codename='delete_recette'),
    Permission.objects.get(codename='add_recette')
)'''
'''
# To get a group:
author = Group.objects.get(name='author')
# To get all users in a group: (as a QuerySet)
authors = author.user_set.all()
'''