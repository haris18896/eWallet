# Generated by Django 3.1 on 2020-09-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_remove_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]