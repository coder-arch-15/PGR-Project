# Generated by Django 3.1.4 on 2021-01-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_user_indian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pending',
            field=models.IntegerField(default=1),
        ),
    ]
