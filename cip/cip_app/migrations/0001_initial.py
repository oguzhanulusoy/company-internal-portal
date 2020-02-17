# Generated by Django 3.0 on 2020-02-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(help_text='Citizenship number', max_length=11, unique=True, verbose_name='Identifier')),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], help_text='Gender', max_length=6, verbose_name='Sex')),
                ('birth_date', models.DateField(help_text='Birthdate', verbose_name='Birthdate')),
            ],
        ),
    ]