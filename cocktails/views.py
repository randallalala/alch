from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from cocktails.models import Cocktail
from .models import Cocktail
from .forms import CocktailForm


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
  fields = ['name', 'notes', 'ingredients', 'alcohol_content']
# alcohol_content
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
class CocktailUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Cocktail
  fields = ['name', 'notes', 'ingredients', 'alcohol_content']
  def test_func(self):
    cocktail = self.get_object()
    return self.request.user == cocktail.author
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
def about(request):
    return render(request, "cocktails/about.html",)
  # {'name':'about us page'}



# class UomDetailView(DetailView):
#   model = models.UOM
# class UomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#   model = models.UOM
#   success_url = reverse_lazy('uoms-home')
#   def test_func(self):
#     uom = self.get_object()
#     return self.request.user == uom.author
# class UomCreateView(LoginRequiredMixin, CreateView):
#   model = models.UOM
#   fields = ['uom']
#   def form_valid(self, form):
#     form.instance.author = self.request.user
#     return super().form_valid(form)
# class UomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#   model = models.UOM
#   fields = ['uom' ]
#   def test_func(self):
#     uom = self.get_object()
#     return self.request.user == uom.author
#   def form_valid(self, form):
#     form.instance.author = self.request.user
#     return super().form_valid(form)
# def about(request):
#     return render(request, "uoms/about.html",)
#   # {'name':'about us page'}



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

# @login_required
# def cocktail_create_view(request):
#     form = ArticleForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         cocktail_object = form.save()
#         context['form'] = ArticleForm()
#         # return redirect("cocktail-detail", slug=cocktail_object.slug)
#         return redirect(cocktail_object.get_absolute_url())
#         # context['object'] = cocktail_object
#         # context['created'] = True
#     return render(request, "cocktails/create.html", context=context)

# def cocktail_create_view(request):
#     # print(request.POST)
#     form = ArticleForm()
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             name = form.cleaned_data.get("name")
#             cocktail_object = Article.objects.create(name=name)
#             context['object'] = cocktail_object
#             context['created'] = True
#     return render(request, "cocktails/create.html", context=context)

def cocktail_search_view(request):
  print(dir(request))
  query_dict = dict(request.GET)
  query = query_dict.get("query")
  try:
    query=int(query_dict.get("q"))
  except:
    query = None
  cocktail_obj = None
  if query is not None:
    cocktail_obj = Cocktail.objects.get(id=query)
  context = { "object": cocktail_obj }
  return render(request, "cocktails/search.html", context=context)
    #  "cocktail/search.html"
    
def cocktail_detail_view(request, id=None):
  cocktail_obj = None
  if id is not None:
    cocktail_obj = Cocktail_objects.get(id=id)
  context = { "object": cocktail_obj, }
  return render(request, "cocktails/cocktail_detail.html", context=context)

def home_view(request, *args , **kwargs ):
  print(args, kwargs)
  cocktail_obj = Cocktail.objects.get(id=2)
  cocktail_queryset = Cocktail.objects.all()
  context = {
    'object_list': cocktail_queryset,
    'name': cocktail_obj.name,
    'id': cocktail_obj.id
  }
  
  # H1_STRING = f"""
  # <h1> {cocktail_obj.name} (id: {cocktail_obj.id}) !</h1>
  # """ 
  # tmpl = get_template("home.html")
  # tmpl_string = tmpl.render(context=context)
  
  HTML_STRING = render_to_string("cocktails/home.html",context=context)
  # HTML_STRING = H1_STRING 
  return HttpResponse(HTML_STRING)

  