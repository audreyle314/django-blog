# Generated by Django 4.2.2 on 2023-06-12 03:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
