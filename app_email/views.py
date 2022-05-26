from django.shortcuts import render, redirect
from django.core.mail import send_mail
from app_list.models import Request

# Create your views here.

def send_email (request):
    current_request=Request.objects.latest('created')
    request_dateTime=current_request.created
    request_dateTime=request_dateTime.strftime('%Y-%m-%dT%H:%M')

    send_mail (
        #subject
        'Заявка Ростелеком ' + request_dateTime,
        #message
        #'ФИО: ' + current_request.f_name +' '+ current_request.l_name + '\n' + 
        'ФИО: ' + current_request.f_name +'\n' + 
        'Телефон: ' + current_request.phone + '\n' +
        'Район: ' + current_request.region + '\n' +
        'Город: ' + current_request.city + '\n' +
        'Улица: ' + current_request.street + '\n' +
        'Дом # ' + current_request.building + '\n',
        #'Квартира # ' + current_request.appartment,
        #from
        '79200711112@yandex.ru',
        #to
        ['sergei_vinokurov@rambler.ru'],
        fail_silently=False    
    )
    return redirect ('home')

