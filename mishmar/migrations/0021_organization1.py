# Generated by Django 3.2.8 on 2022-02-20 10:16

from django.db import migrations, models
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mishmar', '0020_auto_20220220_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('num_weeks', models.IntegerField(default=2)),
                ('published', models.BooleanField(default=False, verbose_name='פרסום')),
                ('weeks_data', jsonfield.fields.JSONField()),
            ],
            options={
                'verbose_name': 'סידור עבודה',
                'verbose_name_plural': 'סידורי עבודה',
            },
        ),
    ]
