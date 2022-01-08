from django.contrib import admin

# Register your models here.
from . models import API, Biodata

class BiodataAdmin(admin.ModelAdmin):
    list_display = ('user','nama','telp','alamat')
admin.site.register(Biodata, BiodataAdmin)

class APIAdmin(admin.ModelAdmin):
    list_display = ('user', 'api_key')
admin.site.register(API, APIAdmin)