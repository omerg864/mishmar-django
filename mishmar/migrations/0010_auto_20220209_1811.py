# Generated by Django 3.2.8 on 2022-02-09 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mishmar', '0009_delete_settings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='after_noon',
        ),
        migrations.RemoveField(
            model_name='event',
            name='morning',
        ),
        migrations.RemoveField(
            model_name='event',
            name='night',
        ),
        migrations.RemoveField(
            model_name='event',
            name='night_before',
        ),
        migrations.RemoveField(
            model_name='event',
            name='training',
        ),
    ]
