from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# from decimal import Decimal

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

# meta? proxy? depends on? manytomanyfield?

class UOM(models.Model):
  uom = models.TextField(unique=True)
  def __str__(self):
    return self.uom

class Quantity(models.Model):
  quantity = models.DecimalField(max_digits=4, decimal_places=0)
  def __str__(self):
    return self.quantity
  
class Ingredient(models.Model):
  name = models.TextField(unique=True)
  # uom = models.ManyToManyField(UOM)
  alcohol_content = models.DecimalField(max_digits=3, decimal_places=0, validators=PERCENTAGE_VALIDATOR, blank=False)
  def __str__(self):
    return self.name

class Cocktail(models.Model):
  name = models.CharField(max_length=100, unique=True)
  notes = models.TextField(blank=True)
  # ingredients = models.ManyToManyField(Ingredient)
  uom = models.ForeignKey(UOM, on_delete=models.SET_NULL, blank=True, null=True) 
  quantity = models.ForeignKey(Quantity, on_delete=models.SET_NULL, blank=True, null=True)
  ingredients = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, blank=True, null=True) 
  # ingredients = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, blank=True, null=True) 
  author = models.ForeignKey(User, on_delete=models.CASCADE) 
  def get_absolute_url(self):
    return reverse("cocktails-detail", kwargs={"pk": self.pk})
  def __str__(self):
    return self.name


  # DELETE CASCADE - IF USER DELETED, DELETE ALL COCKTAILS
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
