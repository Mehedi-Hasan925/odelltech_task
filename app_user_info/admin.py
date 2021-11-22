from django.contrib import admin
from app_user_info import models

#modelAdmin
class user_info_admin(admin.ModelAdmin):
    list_display = ['name','country','Division','District','upazilla']
    class Media:
        js = ("js/ajax.js",)

# Register your models here.
admin.site.register(models.Country)
admin.site.register(models.Divisions)
admin.site.register(models.Districts)
admin.site.register(models.Upazilla)
admin.site.register(models.User_info,user_info_admin)