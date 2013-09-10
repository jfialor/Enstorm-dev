from models import Type
from django.contrib import admin

class AdminType(admin.ModelAdmin):
    pass
    
admin.site.register(Type, AdminType)