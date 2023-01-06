from django.urls import path
from . import views

urlpatterns = [
    path('', views.CocktailListView.as_view(), name="cocktails-home"),
    path('cocktail/<int:pk>', views.CocktailDetailView.as_view(), name="cocktails-detail"),
    path('cocktail/create', views.CocktailCreateView.as_view(), name="cocktails-create"),
    path('cocktail/<int:pk>/update', views.CocktailUpdateView.as_view(), name="cocktails-update"),
    path('cocktail/<int:pk>/delete', views.CocktailDeleteView.as_view(), name="cocktails-delete"),
    path('about/', views.about, name="cocktails-about"),
    
    path('uom/<int:pk>', views.UomDetailView.as_view(), name="uoms-detail"),
    path('uom/create', views.UomCreateView.as_view(), name="uoms-create"),
    path('uom/<int:pk>/update', views.UomUpdateView.as_view(), name="uoms-update"),
    path('uom/<int:pk>/delete', views.UomDeleteView.as_view(), name="uoms-delete"),
    
    path('ingredient/<int:pk>', views.IngredientDetailView.as_view(), name="ingredients-detail"),
    path('ingredient/create', views.IngredientCreateView.as_view(), name="ingredients-create"),
    path('ingredient/<int:pk>/update', views.IngredientUpdateView.as_view(), name="ingredients-update"),
    path('ingredient/<int:pk>/delete', views.IngredientDeleteView.as_view(), name="cocktails-delete"),
]