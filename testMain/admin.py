from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Url_service)
class Url_serviceAdmin(admin.ModelAdmin):
    list_display = ['url','short_url','created_at','user']
