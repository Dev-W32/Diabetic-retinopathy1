# Generated by Django 4.1.3 on 2022-11-28 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_detect_left_eye_remove_detect_right_eye'),
    ]

    operations = [
        migrations.DeleteModel(
            name='detect',
        ),
    ]