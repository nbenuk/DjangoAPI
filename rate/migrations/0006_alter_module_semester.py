# Generated by Django 4.0.2 on 2022-02-23 15:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0005_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='semester',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)]),
        ),
    ]