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
