# Generated by Django 3.1.4 on 2021-01-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20210120_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(null='False'),
        ),
    ]
