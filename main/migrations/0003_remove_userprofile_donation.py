# Generated by Django 4.0.1 on 2022-02-08 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userprofile_donation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='donation',
        ),
    ]
