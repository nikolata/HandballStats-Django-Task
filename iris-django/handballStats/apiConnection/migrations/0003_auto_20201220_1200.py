# Generated by Django 3.1.4 on 2020-12-20 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiConnection', '0002_auto_20201220_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='opponents',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]
