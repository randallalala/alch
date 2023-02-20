from django.contrib import admin
from .models import Ingredient, Cocktail
# another method.. or organize models
# from .models import UOM, Ingredient, Cocktail

# Register your models here.
# admin.site.register(models.UOM)

class IngredientInline(admin.StackedInline):
  model = Ingredient
  fields = ['cocktail','name','alcohol_content', 'quantity', 'unit']
  
class CocktailAdmin(admin.ModelAdmin):
  inlines = [IngredientInline]
  list_display = ['name','author']
  readonly_fiels = ['timestamp', 'updated']
  raw_id_fields = ['author']
  
admin.site.register(models.Ingredient)
admin.site.register(models.Cocktail)
  