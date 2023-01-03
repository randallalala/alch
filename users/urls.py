from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cocktails.urls')),
    path('register/', user_views.register, name="user-register"),
]
