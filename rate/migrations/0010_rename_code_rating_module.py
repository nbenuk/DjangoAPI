# Generated by Django 4.0.2 on 2022-03-08 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0009_rename_profesesor_rating_professor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='code',
            new_name='module',
        ),
    ]