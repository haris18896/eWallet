# Generated by Django 3.1 on 2020-09-18 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_auto_20200918_0813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='username',
        ),
    ]