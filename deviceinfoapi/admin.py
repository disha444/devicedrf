from django.contrib import admin
from .models import Devicinfo


@admin.register(Devicinfo)
class Deviceadmin(admin.ModelAdmin):
    list_display = ['id','device_name','device_price']
