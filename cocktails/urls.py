from django.urls import path
from . import views

urlpatterns = [
    path('', views.CocktailListView.as_view(), name="cocktails-home"),
    path('cocktail/<int:pk>', views.CocktailDetailView.as_view(), name="cocktails-detail"),
    path('cocktail/create', views.CocktailCreateView.as_view(), name="cocktails-create"),
    path('cocktail/<int:pk>/update', views.CocktailUpdateView.as_view(), name="cocktails-update"),
    path('cocktail/<int:pk>/delete', views.CocktailDeleteView.as_view(), name="cocktails-delete"),
    path('about/', views.about, name="cocktails-about"),
]