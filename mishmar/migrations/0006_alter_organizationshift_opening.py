# Generated by Django 3.2.8 on 2022-02-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mishmar', '0005_auto_20220207_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationshift',
            name='opening',
            field=models.BooleanField(blank=True, default=False, verbose_name='פתיחה'),
        ),
    ]
