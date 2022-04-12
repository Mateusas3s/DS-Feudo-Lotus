from django.urls import path
from .views import daily_Pag, dailyCreate
from .views import formDailyCreate, formDailyUpdate, dailyUpdate
from .views import dailyDelete
from .views import dailyList
from . import views

urlpatterns=[
    path('', daily_Pag.as_view(), name='pagina-daily'),
    #create
    path('create/date', views.dailyCreate, name='daily-day'),
    path('create/form', views.formDailyCreate, name='form-daily'),
    #update
    path('update/date/<int:pk>', views.dailyUpdate, name='daily-day-update'),
    path('update/form/<int:pk>', views.formDailyUpdate, name='update-daily'),
    #delete
    path('delete/date/<int:pk>', dailyDelete.as_view(), name='daily-day-delete'),
    #list
    path('list/date/', dailyList.as_view(), name='lista-date'),
    path('list/dailys/', views.contribList, name='lista-dailys'),
]