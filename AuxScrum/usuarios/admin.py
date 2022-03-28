from pyexpat import model
from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['user', 'nome_completo', 'telefone']
    search_fields = ['user']
    list_filter = ['user']
    save_on_top = True

admin.site.register(UserProfile, UserProfileAdmin)