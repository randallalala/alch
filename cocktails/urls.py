from django.urls import path
from .views import home_view
from . import views
# from . import (

    # cocktail_list_view,
    # cocktail_detail_view,
    # cocktail_delete_view,
    # cocktail_create_view,
    # cocktail_update_view,
    # cocktail_detail_hx_view,
    # cocktail_ingredient_update_hx_view,
    # cocktail_incredient_delete_view,
    # cocktail_ingredient_image_upload_view
    # )  
# re_path  >> regex url pattern

# app_name='cocktails'


urlpatterns = [
    # after views, CocktailListView etc is the function
    path('', views.CocktailListView.as_view(), name="cocktails-home"),
    path('cocktail/<int:pk>', views.CocktailDetailView.as_view(), name="cocktails-detail"),
    path('cocktail/create', views.CocktailCreateView.as_view(), name="cocktails-create"),
    path('cocktail/<int:pk>/update', views.CocktailUpdateView.as_view(), name="cocktails-update"),
    path('cocktail/<int:pk>/delete', views.CocktailDeleteView.as_view(), name="cocktails-delete"),
    path('about/', views.about, name="cocktails-about"),
    
    
    # path('uom/<int:pk>', views.UomDetailView.as_view(), name="uoms-detail"),
    # path('uom/create', views.UomCreateView.as_view(), name="uoms-create"),
    # path('uom/<int:pk>/update', views.UomUpdateView.as_view(), name="uoms-update"),
    # path('uom/<int:pk>/delete', views.UomDeleteView.as_view(), name="uoms-delete"),
    
    path('ingredient/<int:pk>', views.IngredientDetailView.as_view(), name="ingredients-detail"),
    path('ingredient/create', views.IngredientCreateView.as_view(), name="ingredients-create"),
    path('ingredient/<int:pk>/update', views.IngredientUpdateView.as_view(), name="ingredients-update"),
    path('ingredient/<int:pk>/delete', views.IngredientDeleteView.as_view(), name="cocktails-delete"),

    # path('results', views.detail_view, name="results"),
# 
# int / str - for id matters
    # path("", home_view),
    path("cocktails/", views.cocktail_search_view ),
    path("cocktails/<int:id>/", views.cocktail_detail_view ),
    # path('search', views.cocktail_search_view, name="search"),
    # path('search/<int:id>', views.search_view, name="cocktails-search"),
    # path("", cocktail_list_view, name='list'),
    # path("create/", cocktail_create_view, name='create'),
    
    # path("hx/<int:parent_id>/ingredient/<int:id>/", cocktail_ingredient_update_hx_view, name='hx-ingredient-detail'),
    # path("hx/<int:parent_id>/ingredient/", cocktail_ingredient_update_hx_view, name='hx-ingredient-create'),
    # path("hx/<int:id>/", cocktail_detail_hx_view, name='hx-detail'),
    
    # path("<int:parent_id>/image-upload/", cocktail_ingredient_image_upload_view, name='cocktail-ingredient-image-upload'),
    # path("<int:parent_id>/ingredient/<int:id>/delete/", cocktail_incredient_delete_view, name='ingredient-delete'),
    # path("<int:id>/delete/", cocktail_delete_view, name='delete'),
    # path("<int:id>/edit/", cocktail_update_view, name='update'),
    # path("<int:id>/", cocktail_detail_view, name='detail'),

]


