# Generated by Django 4.2.6 on 2023-10-20 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_catgoery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catgoery',
            new_name='Category',
        ),
    ]
