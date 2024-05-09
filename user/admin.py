from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Kişisel Bilgiler',{'fields':['birth_date','phone']}),)

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('title','owner')

admin.site.register(Profil,ProfilAdmin)
admin.site.register(CustomUser,CustomUserAdmin)