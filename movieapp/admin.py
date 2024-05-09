from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Favoriler)

