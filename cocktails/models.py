import pathlib
import pint
import uuid

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# from django import pint
# from decimal import Decimal
from django.utils.text import slugify


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

# meta? proxy? depends on? manytomanyfield?

# class UOM(models.Model):
#   uom = models.TextField(unique=True)
#   def __str__(self):
#     return self.uom

# class Quantity(models.Model):
#   quantity = models.DecimalField(max_digits=4, decimal_places=0)
#   def __str__(self):
#     return self.quantity
  

class Cocktail(models.Model):
  name = models.CharField(max_length=100, unique=True)
  slug = models.SlugField(blank=True, null=True)
  notes = models.TextField(blank=True)
  # ingredients = models.ManyToManyField(Ingredient)
  # ingredients = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, blank=True, null=True) 
  author = models.ForeignKey(User, on_delete=models.CASCADE) 
  def get_absolute_url(self):
    return reverse("cocktails-detail", kwargs={"pk": self.pk})
  def __str__(self):
    return self.name
  def save(self, *args, **kwargs):
    if self.slug is None:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  # DELETE CASCADE - IF USER DELETED, DELETE ALL COCKTAILS
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)


class Ingredient(models.Model):
  # cocktail = models.ForeignKey(Cocktail)
  cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
  name = models.TextField(unique=True)
  alcohol_content = models.DecimalField(max_digits=3, decimal_places=0, validators=PERCENTAGE_VALIDATOR, blank=False)
  # uom = models.ForeignKey(UOM, on_delete=models.SET_NULL, blank=True, null=True) 
  quantity = models.CharField(max_length=50)
  unit = models.CharField(max_length=50)
  # quantity = models.ForeignKey(Quantity, on_delete=models.SET_NULL, blank=True, null=True)

  def __str__(self):
    return self.name
