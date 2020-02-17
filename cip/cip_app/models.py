from django.db import models

# Calls abstract Django user model
from django.contrib.auth.models import User

# Retrieves all lists from list.py
from .lists import *

class Person(models.Model):

    # This is a bound between Person and User model
    # that is inherited from abstract Django user model.
    # It is never null or blank.
    identifier = models.CharField(verbose_name='Identifier', unique=True, blank=False, null=False, help_text='Citizenship', max_length=11)

    # This is a list that includes two options about sex.
    sex = models.CharField(verbose_name='Sex', unique=False, blank=False, null=False, help_text='Gender', max_length=6, choices=SEX)

    # This is date field for date of birth.
    birth_date = models.DateField(verbose_name='Birthdate', unique=False, blank=False, null=False, help_text='Birthdate', auto_now=False)

    # @important: Choice must be redefined.
    # This is a city for place of birth.
    birth_place = models.CharField(verbose_name='Birth place', unique=False, blank=False, null=False, help_text='Birth place', max_length=6, choices=SEX, default=SEX[0])

    # @important: Choice must be redefined.
    # This is a list that includes marital statues.
    marital_status = models.CharField(verbose_name='Marital status', unique=False, blank=False, null=False, help_text='Marital status', max_length=6, choices=SEX, default=SEX[0])

    # @important: Choice must be redefined.
    # This is a list that includes blood types.
    blood_types = models.CharField(verbose_name='Blood types', unique=False, blank=False, null=False, help_text='Blood types', max_length=6, choices=SEX, default=SEX[0])

    # This is a field that store address within maximum 100 characters.
    address = models.CharField(verbose_name='Address', unique=False, blank=True, null=True, help_text='Max 100 chars.', max_length=100)

    town = models.CharField(verbose_name='Town', unique=False, blank=True, null=True, help_text='Max 100 chars.', max_length=100)

    city = models.CharField(verbose_name='City', unique=False, blank=True, null=True, help_text='Max 100 chars.', max_length=100)







