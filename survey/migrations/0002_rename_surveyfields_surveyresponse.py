# Generated by Django 4.0.4 on 2022-05-15 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SurveyFields',
            new_name='SurveyResponse',
        ),
    ]
