from django.contrib import admin
from . models import ChannelGroup, Request, Tariff, Channel, ChannelGroup

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'phone', 'f_name', 'l_name', 'region', 'city')

class TariffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'technology', 'speed', 'tv', 'wink', 'yandex', 'price')

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'thumbnail_file')

class ChannelGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Request, RequestAdmin)
admin.site.register(Tariff, TariffAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(ChannelGroup, ChannelGroupAdmin)





