# Generated by Django 4.2.5 on 2023-11-16 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='main_id',
            new_name='idf',
        ),
    ]
