from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('channels', views.channels, name='channels'),
    path('technology', views.technology, name='technology'),
    path('create_new_request', views.create_new_request, name='create_new_request'),
]
