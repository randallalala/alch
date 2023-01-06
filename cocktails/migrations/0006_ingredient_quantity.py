# Generated by Django 4.1.4 on 2023-01-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "cocktails",
            "0005_remove_cocktail_ingredients_remove_ingredient_uom_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredient",
            name="quantity",
            field=models.DecimalField(
                blank=True, decimal_places=0, default=1, max_digits=3
            ),
            preserve_default=False,
        ),
    ]
