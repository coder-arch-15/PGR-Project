# Generated by Django 3.1.4 on 2021-01-16 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_user_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
