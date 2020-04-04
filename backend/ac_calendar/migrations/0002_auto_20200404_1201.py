# Generated by Django 3.0.5 on 2020-04-04 12:01

from django.db import migrations

preset_categories = [
    {"name": "anime", "order": 0},
    {"name": "comic", "order": 1},
    {"name": "future", "order": 2},
]


def data_migrate(apps, schema_editor):
    Category = apps.get_model("ac_calendar", "Category")
    for category in preset_categories:
        Category.objects.get_or_create(**category)


def reverse(apps, schema_editor):
    Category = apps.get_model("ac_calendar", "Category")
    for category in preset_categories:
        Category.objects.filter(name=category['name']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('ac_calendar', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(data_migrate, reverse)
    ]