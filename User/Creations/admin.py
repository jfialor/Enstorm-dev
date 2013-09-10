from django.contrib import admin

from creationgroups.Media import*


class GroupAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(Group, GroupAdmin)
