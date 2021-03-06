from django.db import models

# Calls abstract Django user model
from django.contrib.auth.models import User

# Retrieves all lists from list.py
from .lists import *

class Person(models.Model):

    # Proxy design pattern is applied by Django model.
    Proxy = True

    # This is a bound between Person and User model
    # that is inherited from abstract Django user model.
    # It is never null or blank.
    identifier = models.CharField(verbose_name='Identifier', unique=True, blank=False, null=False, help_text='Citizenship', max_length=11)

    # A list that includes two options about sex.
    sex = models.CharField(verbose_name='Sex', unique=False, blank=False, null=False, help_text='Gender', max_length=6, choices=SEX)

    # Date field for date of birth.
    birth_date = models.DateField(verbose_name='Birthdate', unique=False, blank=False, null=False, help_text='Birthdate', auto_now=False)

    # @important: Choice must be redefined.
    # A city for place of birth.
    birth_place = models.CharField(verbose_name='Birth place', unique=False, blank=False, null=False, help_text='Birth place', max_length=6, choices=SEX, default=SEX[0])

    # @important: Choice must be redefined.
    # A list that includes marital statues.
    marital_status = models.CharField(verbose_name='Marital status', unique=False, blank=False, null=False, help_text='Marital status', max_length=6, choices=SEX, default=SEX[0])

    # @important: Choice must be redefined.
    # A list that includes blood types.
    blood_types = models.CharField(verbose_name='Blood types', unique=False, blank=False, null=False, help_text='Blood types', max_length=6, choices=SEX, default=SEX[0])

    # A field that stores address within maximum 100 characters.
    address = models.CharField(verbose_name='Address', unique=False, blank=True, null=True, help_text='Max 100 chars.', max_length=100)

    # @important: Choice must be redefined.
    # A field that stores town as free text.
    town = models.CharField(verbose_name='Town', unique=False, blank=True, null=True, help_text='Max 100 chars.', max_length=100)

    # @important: Choice must be redefined.
    # A list that includes cities in Turkey.
    city = models.CharField(verbose_name='City', unique=False, blank=True, null=True, help_text='Select from list.', max_length=100, choices=SEX, default=SEX[0])

    # Date field for entrance to social security.
    date_for_social_security = models.DateField(verbose_name='D4SS', unique=False, blank=False, null=False, help_text='Date for social security', auto_now=False)

    # A field that stores mobile phone within prefix.
    mobile_phone = models.CharField(verbose_name='Mobile phone', unique=False, blank=True, null=True, help_text='05373119592', max_length=11)

    # A field that stores militaryship status just for men.
    militaryship = models.BooleanField(verbose_name='Military status', unique=False, blank=True, null=True, help_text='Just for male', default=False)

    # @important: The part that stars from here ends within partner_company field
    # should be divided into another table.
    # A field that stores partner's name
    partner_name = models.CharField(verbose_name='Partner name', unique=False, blank=True, null=True, help_text='Name for husband or wife', max_length=20)

    # A list that includes two options about sex.
    partner_sex = models.CharField(verbose_name='Partner sex', unique=False, blank=False, null=False, help_text='Gender', max_length=6, choices=SEX)

    # A field that stores partner's birth date
    partner_birth_date = models.DateField(verbose_name='Partner birthdate', unique=False, blank=False, null=False, help_text='Birthdate', auto_now=False)

    # A field that stores partner's citizenship number
    partner_identifier = models.CharField(verbose_name='Partner citizenship number', unique=True, blank=False, null=False, help_text='Citizenship', max_length=11)

    # A field that stores partner's company
    partner_company = models.CharField(verbose_name='Partner company', unique=False, blank=True, null=True, help_text='Where is she working', max_length=100)

    # A field that stores employee' emergency information
    emergency_calls = models.CommaSeparatedIntegerField(verbose_name='Emergency calls', unique=False, blank=True, null=True)

    '''
    Eğitim bilgileri yer alacak    
    Yabancı dil bilgileri yer alacak

    '''

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return str(self.identifier)

class EmergencyInformation(models.Model):

    # Proxy design pattern is applied by Django model.
    Proxy = True

    # This table -EmergencyInformation- includes some information
    # for emergency situation. It stores first name, last name,
    # relationship, phone number.
    first_name = models.CharField(verbose_name='First name', unique=False, blank=True, null=True, help_text='Emergency call', max_length=20)



