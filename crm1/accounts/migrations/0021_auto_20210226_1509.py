# Generated by Django 3.1.4 on 2021-02-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20210226_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='theme',
            field=models.CharField(choices=[('Light', 'Light'), ('Dark', 'Dark')], default='Light', max_length=200, null=True),
        ),
    ]
