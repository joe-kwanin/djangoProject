# Generated by Django 4.0.1 on 2022-12-05 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_categorie'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categorie',
            new_name='categories',
        ),
    ]
