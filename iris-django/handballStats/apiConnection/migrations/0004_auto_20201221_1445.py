# Generated by Django 3.1.4 on 2020-12-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiConnection', '0003_auto_20201220_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='team',
            name='last_match',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='team',
            name='last_win',
            field=models.DateTimeField(auto_now=True),
        ),
    ]