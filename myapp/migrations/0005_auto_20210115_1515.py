# Generated by Django 3.1.4 on 2021-01-15 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210115_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phonenumber',
            new_name='phone',
        ),
    ]
