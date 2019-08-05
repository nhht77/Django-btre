from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listing

# Create your views here.
def index(request):

    listings  = Listing.objects.all()
    paginator = Paginator(listings, 3)

    page      = request.GET.get('page')
    paged_listing = paginator.get_page(page) 

    context = {'listings': paged_listing}
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')