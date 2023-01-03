from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cocktail(models.Model):
  name = models.CharField(max_length=100)
  notes = models.TextField(blank=True)
  ingredients = models.TextField()
  alcohol_content = models.TextField()
  
  # DELETE CASCADE - IF USER DELETED, DELETE ALL COCKTAILS
#   author = models.ForeignKey(User, on_delete=models.CASCADE) 

#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
