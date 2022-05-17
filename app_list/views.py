from django.shortcuts import render, redirect
from .models import Request

# Create your views here.
def home (request):
    return render (request, 'home.html')

def create_new_request(request):
    if request.method=="POST":
        f_name = request.POST["f_name"]
        l_name = request.POST["l_name"]
        phone = request.POST["phone"]
        region = request.POST["region"]
        city = request.POST["city"]
        street = request.POST["street"]
        building = request.POST["building"]
        appartment = request.POST["appartment"]

        request=Request.objects.create(
            f_name=f_name,
            l_name=l_name,
            phone=phone,
            region=region,
            city=city,
            street=street,
            building=building,
            appartment=appartment
        )

        return redirect ('send_email')

