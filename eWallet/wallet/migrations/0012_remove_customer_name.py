# Generated by Django 3.1 on 2020-09-18 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_auto_20200918_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
