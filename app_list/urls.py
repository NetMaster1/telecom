from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('channels', views.channels, name='channels'),
    path('technology', views.technology, name='technology'),
    path('agreement', views.agreement, name='agreement'),
    path('create_new_request', views.create_new_request, name='create_new_request'),
    path('tarif/<int:tarif_id>', views.tarif, name='tarif'),
]
