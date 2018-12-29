from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_publish=True)[:3]
    context =  {
        'listings' : listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    #get al realtor
    realtors = Realtor.objects.order_by('-hire_date')
    #get realtor of the onth
    mvps = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvps': mvps
    }
    return render(request, 'pages/about.html', context)