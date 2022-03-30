from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PaginaInicial


urlpatterns = [
    #path('', view, name=''),
    path('home/', PaginaInicial.as_view(), name='home'),
]