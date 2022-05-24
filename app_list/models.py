from django.db import models

# Create your models here.


class Request (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250, null=True)
    region = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    street = models.CharField(max_length=250, null=True)
    building = models.CharField(max_length=250,null=True)
    appartment = models.CharField(max_length=250, null=True)

    def __int__(self):
        return self.id

class Tariff (models.Model):
    name = models.CharField(max_length=250)
    technology = models.CharField(max_length=10, null=True)
    speed = models.CharField(max_length=10, default='100 Мб/сек')
    tv = models.BooleanField(default=True)
    wink = models.BooleanField(default=True)
    yandex = models.BooleanField(default=False)
    price=models.IntegerField(default=0)

    def __int__(self):
        return self.id

class ChannelGroup (models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Channel (models.Model):
    name = models.CharField(max_length=250)
    group = models.ForeignKey(ChannelGroup, null=True, on_delete=models.DO_NOTHING)
    thumbnail_file = models.ImageField(upload_to='uploads')

    def __int__(self):
        return self.id


