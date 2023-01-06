from django.contrib import admin
from . import models
# from .models import UOM, Ingredient, Cocktail

# Register your models here.
admin.site.register(models.UOM)
admin.site.register(models.Ingredient)
admin.site.register(models.Cocktail)
