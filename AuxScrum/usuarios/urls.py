from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PaginaInicial, UsuarioCreate

urlpatterns = [
    #path('', view, name=''),
    path('', PaginaInicial.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(
            template_name='usuarios/formLogin.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', UsuarioCreate.as_view(), name='cadastro'),
]