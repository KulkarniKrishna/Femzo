# Generated by Django 3.2.7 on 2022-04-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0026_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]