# Generated by Django 3.2.8 on 2022-02-20 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mishmar', '0022_alter_shift_organization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shift',
            old_name='username',
            new_name='user',
        ),
    ]
