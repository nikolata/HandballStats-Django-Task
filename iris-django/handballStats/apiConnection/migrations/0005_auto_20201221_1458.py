# Generated by Django 3.1.4 on 2020-12-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiConnection', '0004_auto_20201221_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='last_win',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
