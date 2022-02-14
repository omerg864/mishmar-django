# Generated by Django 3.2.8 on 2022-02-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usersettings_fri_noon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersettings',
            name='sat_noon',
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='sat_morning',
            field=models.IntegerField(default=0, verbose_name='שבת בוקר/צהריים'),
        ),
    ]
