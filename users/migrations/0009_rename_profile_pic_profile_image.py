# Generated by Django 3.2 on 2021-07-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_image_profile_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='image',
        ),
    ]
