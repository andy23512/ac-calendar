# Generated by Django 3.0.5 on 2020-05-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ac_calendar', '0002_auto_20200404_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='next_episode_date',
            field=models.DateField(null=True),
        ),
    ]