from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

# Create your views here.
def index(request):
    listings= Listing.objects.order_by('-list_date').filter(is_publish=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context={
        'listings': paged_listings
    }


    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    indv_listing = get_object_or_404(Listing, pk = listing_id)

    context = {
        'listing': indv_listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')