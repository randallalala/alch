from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Cocktail(models.Model):
  name = models.CharField(max_length=100)
  notes = models.TextField(blank=True)
  ingredients = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE) 
  alcohol_content = models.TextField()
  
  def get_absolute_url(self):
    return reverse("cocktails-detail", kwargs={"pk": self.pk})

  
  # DELETE CASCADE - IF USER DELETED, DELETE ALL COCKTAILS
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
