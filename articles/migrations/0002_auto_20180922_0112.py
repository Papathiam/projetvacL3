# Generated by Django 2.1.1 on 2018-09-22 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='articles',
        ),
    ]