# Generated by Django 2.2.2 on 2019-06-29 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20190629_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='gener',
            new_name='genre',
        ),
    ]
