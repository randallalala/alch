from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# from decimal import Decimal

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class UOM(models.Model):
  uom = models.TextField(unique=True)
  def __str__(self):
    return self.uom

class Ingredient(models.Model):
  name = models.TextField(unique=True)
  alcohol_content = models.DecimalField(max_digits=3, decimal_places=0, validators=PERCENTAGE_VALIDATOR,blank=False)
  # uom = models.ManyToManyField(UOM)
  uom = models.ForeignKey(UOM, on_delete=models.SET_NULL,blank=True,null=True) 
  def __str__(self):
    return self.name

class Cocktail(models.Model):
  name = models.CharField(max_length=100, unique=True)
  notes = models.TextField(blank=True)
  # ingredients = models.TextField()
  # ingredients = models.ManyToManyField(Ingredient)
  ingredients = models.ForeignKey(Ingredient, on_delete=models.SET_NULL,blank=True,null=True) 
  author = models.ForeignKey(User, on_delete=models.CASCADE) 
  # alcohol_content = models.TextField()
  def get_absolute_url(self):
    return reverse("cocktails-detail", kwargs={"pk": self.pk})
  def __str__(self):
    return self.name


  # DELETE CASCADE - IF USER DELETED, DELETE ALL COCKTAILS
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
