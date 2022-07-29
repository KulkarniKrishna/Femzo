# Generated by Django 3.2.7 on 2022-04-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0028_profiledetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='country',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='postcode',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='state',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='profiledetails',
            name='uemail',
            field=models.EmailField(default='', max_length=20),
        ),
    ]