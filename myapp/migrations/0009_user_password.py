# Generated by Django 3.1.4 on 2021-01-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210115_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='1234test', max_length=15),
        ),
    ]
