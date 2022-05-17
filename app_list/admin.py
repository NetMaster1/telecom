from django.contrib import admin
from . models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'phone', 'f_name', 'l_name', 'region', 'city')

admin.site.register(Request, RequestAdmin)





