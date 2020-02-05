from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .lists import *

class Person(models.Model):
    '''
    USER_ID is an id number that is inherited from django user system.
    We can reach to usernmae, first name, last name, e-mail, password,
    date joined fundamentally through USER_ID element.
    Therefore, we do not need these variables again.
    More information about django user:
    https://docs.djangoproject.com/en/3.0/ref/contrib/auth/
    '''
    USER_ID = models.IntegerField(verbose_name='USER_ID',
                                  null=False,
                                  blank=False,
                                  unique=True)

    CITIZENSHIP_NUMBER = models.CharField(verbose_name='CITIZENSHIP_NUMBER',
                                          max_length=11,
                                          null=False,
                                          blank=False,
                                          unique=True)

    GENDER = models.CharField(verbose_name='GENDER',
                              max_length=6,
                              null=False,
                              blank=False,
                              choices=GENDER)

    BIRTHDAY = models.DateField(verbose_name='BIRTHDAY')

    PHONE_NUMBER_REGEX = RegexValidator(regex=r'^\+(?:[0-9] ?){6,14}[0-9]$',
                                 message='Format: "+905304440044"')

    PHONE_NUMBER = models.CharField(validators=[PHONE_NUMBER_REGEX], max_length=17)

    class Meta:
        verbose_name = 'PERSON'
        verbose_name_plural = 'PEOPLE'
        ordering = ['USER_ID']

    @property
    def get_citizenship_number(self):
        return str(self.CITIZENSHIP_NUMBER)

    @property
    def get_gender(self):
        return str(self.GENDER)

    @property
    def get_birthday(self):
        return str(self.BIRTHDAY)

    @property
    def get_phone_number(self):
        return str(self.PHONE_NUMBER)

