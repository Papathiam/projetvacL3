# Generated by Django 2.1.1 on 2018-09-22 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]
