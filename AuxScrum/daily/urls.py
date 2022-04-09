from django.urls import path
from .views import daily_Pag, dailyCreate
from .views import formDailyCreate, formDailyUpdate, dailyUpdate
from .views import dailyDelete
from .views import dailyList

urlpatterns=[
    path('', daily_Pag.as_view(), name='pagina-daily'),
    #create
    path('create/date', dailyCreate.as_view(), name='daily-day'),
    path('create/form', formDailyCreate.as_view(), name='form-daily'),
    #update
    path('update/date/<int:pk>', dailyUpdate.as_view(), name='daily-day-update'),
    path('update/form/<int:pk>', formDailyUpdate.as_view(), name='update-daily'),
    #delete
    path('delete/date/<int:pk>', dailyDelete.as_view(), name='daily-day-delete'),
    #list
    path('list/date/', dailyList.as_view(), name='lista-date'),
]