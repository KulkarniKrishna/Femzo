# Generated by Django 3.2.7 on 2021-12-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_contactusmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='idprooof',
            field=models.FileField(upload_to='data/id/'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(upload_to='data/images/'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='vedio',
            field=models.FileField(upload_to='data/vedios/'),
        ),
    ]
