from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
from datetime import timedelta
from .forms import MessageForm
# Create your views here.

def index(request):
    testimonies = Testimonies.objects.all()[:3]
    latest_services = Service.objects.filter(date_delivered__gte=timezone.now() - timedelta(days=7))

    return render(request, 'pages/index.html',
        {
            "testimonies": testimonies,
            "latest_services": latest_services,
        }
    )

def services(request):
    service_type = ServiceType.objects.all()
    return render(request, 'pages/services.html',
        {
            "services_type": service_type,
        }
    )

def about(request):
    workers = Workers.objects.all()
    return render(request, 'pages/about.html',
        {
            "workers": workers,
        }
    )

def contact(request):
    return render(request, 'pages/contact.html',
        {
            "forms": MessageForm(),
        }
    )


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/contact/")
    else:
        form = MessageForm()
        
    return redirect("/contact/")
