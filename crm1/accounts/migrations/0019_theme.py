# Generated by Django 3.1.4 on 2021-02-26 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('Light', 'Light'), ('Dark', 'Dark')], max_length=200, null=True)),
            ],
        ),
    ]
