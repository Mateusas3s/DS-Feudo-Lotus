from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'missoes'

urlpatterns=[
    path('', views.home, name='home'),
    path('<int:missao_id>', views.detalhe, name='detalhe'),
    path('<int:missao_id>', views.detalhe2, name='detalhe2'),
    path('excluir/<int:missao_id>', views.excluir, name='excluir'),
]