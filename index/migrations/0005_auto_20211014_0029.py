# Generated by Django 3.2.7 on 2021-10-13 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_rename_complaint_complaints'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='complaints',
            new_name='complaint',
        ),
        migrations.RenameModel(
            old_name='UserSignUpCredentials',
            new_name='UserSignUpCredential',
        ),
    ]
