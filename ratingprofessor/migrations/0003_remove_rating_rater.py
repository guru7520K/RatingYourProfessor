# Generated by Django 4.1.7 on 2023-04-01 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratingprofessor', '0002_rating_rater'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rater',
        ),
    ]
