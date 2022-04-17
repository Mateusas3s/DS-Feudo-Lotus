from django.urls import path
from .views import daily_Pag, retro_Pag
from .views import dailyDelete, retroDelete
from .views import dailyList, retroList
from . import views

urlpatterns=[
    ##DAILY##
    path('daily/', daily_Pag.as_view(), name='pagina-daily'),
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

    ##RETROSPECTIVA##
    path('retro/', retro_Pag.as_view(), name='pagina-retro'),
    #create
    path('create/retro', views.retroCreate, name='retro-day'),
    path('create/formRetro', views.formRetroCreate, name='form-retro'),
    #update
    path('update/retro/<int:pk>', views.retroUpdate, name='retro-day-update'),
    path('update/formRetro/<int:pk>', views.formRetroUpdate, name='update-retro'),
    #delete
    path('delete/retro/<int:pk>', retroDelete.as_view(), name='retro-day-delete'),
    #list
    path('list/retro/', retroList.as_view(), name='lista-retro'),
    path('list/retros/', views.contribListRetro, name='lista-retros'),
]