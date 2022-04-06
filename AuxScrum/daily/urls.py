from django.urls import path
from .views import dailyCreate

urlpatterns = [
    path('', dailyCreate.as_view(), name='daily')
]