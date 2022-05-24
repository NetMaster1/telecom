from django.shortcuts import render, redirect
from .models import Request, Tariff, Channel

# Create your views here.
def home (request):
    tariffs=Tariff.objects.all().order_by('price')
    context = {
            'tariffs': tariffs
        }
    return render (request, 'home.html', context)

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
        
def channels (request):
    channels=Channel.objects.all()
    contex={
        'channels': channels
    }
    return render (request, 'channels.html', contex)

def technology (request):
    return render (request, 'technology.html')

def agreement (request):
    return render (request, 'agreement.html')

def tarif (request, tarif_id):
    tarif=Tariff.objects.get(id=tarif_id)
    context ={
        'tarif': tarif
    }
    return render (request, 'tarif.html', context)

