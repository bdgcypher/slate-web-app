# Generated by Django 3.1.4 on 2021-01-19 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_customer_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_created',
        ),
    ]
