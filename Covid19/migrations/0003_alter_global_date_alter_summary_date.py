# Generated by Django 4.0 on 2021-12-29 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Covid19', '0002_alter_country_countrycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='global',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='summary',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
