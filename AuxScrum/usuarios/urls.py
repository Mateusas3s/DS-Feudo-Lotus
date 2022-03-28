from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate
from . import views

urlpatterns = [
    #path('', view, name=''),
    path('', auth_views.LoginView.as_view(
            template_name='usuarios/formLogin.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', UsuarioCreate.as_view(), name='cadastro'),
    path('edit_profile/<int:user_id>', views.edit_profile, name='edit_profile'),
    path('salvarProfile/<int:user_id>', views.salvarProfile, name='salvarProfile'),
]