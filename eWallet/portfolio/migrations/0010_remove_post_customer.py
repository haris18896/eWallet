# Generated by Django 3.1 on 2020-09-16 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20200916_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='customer',
        ),
    ]