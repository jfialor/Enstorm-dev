from models import ShelfType
from django.contrib import admin

class AdminShelfType(admin.ModelAdmin):
    pass
    
admin.site.register(ShelfType, AdminShelfType)