# Generated by Django 3.2.8 on 2022-02-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mishmar', '0012_auto_20220212_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='armingrequest',
            name='input_num',
            field=models.IntegerField(default=1, verbose_name='מספר הזנה'),
        ),
    ]
