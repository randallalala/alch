# Generated by Django 4.1.4 on 2022-12-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cocktails", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cocktail",
            name="author",
        ),
        migrations.AlterField(
            model_name="cocktail",
            name="notes",
            field=models.TextField(blank=True),
        ),
    ]
