# Generated by Django 5.1 on 2024-10-12 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_userprofile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
    ]
