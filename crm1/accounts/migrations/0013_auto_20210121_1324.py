# Generated by Django 3.1.4 on 2021-01-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_order_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
