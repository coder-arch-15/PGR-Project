# Generated by Django 3.1.4 on 2021-01-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210115_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='approved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='pending',
            field=models.IntegerField(default=0),
        ),
    ]
