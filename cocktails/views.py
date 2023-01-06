from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


from . import models

# TEST DATA
# cocktails = [
#   {
#     'name': 'long island tea',
#     'author': 'randa',
#     'ingredients': 'tea',
#     'notes': 'ded',
#     'alcohol_content': '99%'
#   },
#   {
#     'name': 'bloody mary',
#     'author': 'ran',
#     'ingredients': 'tomato',
#     'notes': 'ded', 
#     'alcohol_content': '55%'
#   }
# ]


def home(request):
    cocktails = models.Cocktail.objects.all()
    context = {
        'cocktails': cocktails
    }
    return render(request, "cocktails/home.html", context)

class CocktailListView(ListView):
  model = models.Cocktail
  template_name = 'cocktails/home.html'
  context_object_name = 'cocktails'
class CocktailDetailView(DetailView):
  model = models.Cocktail
class CocktailDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Cocktail
  success_url = reverse_lazy('cocktails-home')
  def test_func(self):
    cocktail = self.get_object()
    return self.request.user == cocktail.author
class CocktailCreateView(LoginRequiredMixin, CreateView):
  model = models.Cocktail
  fields = ['name', 'notes', 'ingredients']
# alcohol_content
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
class CocktailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Cocktail
  fields = ['name', 'notes', 'ingredients', 'alcohol_content' ]
  def test_func(self):
    cocktail = self.get_object()
    return self.request.user == cocktail.author
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
def about(request):
    return render(request, "cocktails/about.html",)
  # {'name':'about us page'}



class UomDetailView(DetailView):
  model = models.UOM
class UomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.UOM
  success_url = reverse_lazy('uoms-home')
  def test_func(self):
    uom = self.get_object()
    return self.request.user == uom.author
class UomCreateView(LoginRequiredMixin, CreateView):
  model = models.UOM
  fields = ['uom']
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
class UomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.UOM
  fields = ['uom' ]
  def test_func(self):
    uom = self.get_object()
    return self.request.user == uom.author
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
def about(request):
    return render(request, "uoms/about.html",)
  # {'name':'about us page'}



class IngredientDetailView(DetailView):
  model = models.Ingredient
class IngredientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Ingredient
  success_url = reverse_lazy('ingredients-home')
  def test_func(self):
    ingredient = self.get_object()
    return self.request.user == ingredient.author
class IngredientCreateView(LoginRequiredMixin, CreateView):
  model = models.Ingredient
  fields = ['name', 'alcohol_content', 'uom', 'quantity']
# alcohol_content
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
class IngredientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Ingredient
  fields = ['name', 'alcohol_content', 'uom', 'quantity']
  def test_func(self):
    ingredient = self.get_object()
    return self.request.user == ingredient.author
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
def about(request):
    return render(request, "ingredients/about.html",)
  # {'name':'about us page'}
  
  
  
# calculate TEST
#- db level / view.py level / template level

# SEARCH TEST 
# https://docs.djangoproject.com/en/4.1/topics/db/search/
# >>> Author.objects.filter(name__contains='Terry')
