from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_new_request', views.create_new_request, name='create_new_request'),
]
