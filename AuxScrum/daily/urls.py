from unicodedata import name
from django.urls import path
from .views import dailyCreate, dailyUpdate

urlpatterns = [
    path('', dailyCreate.as_view(), name='daily'),
    path('update/<int:pk>', dailyUpdate.as_view(), name='update')
]