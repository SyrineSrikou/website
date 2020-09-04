from django.shortcuts import get_object_or_404, render

from .models import Offer

def index(request):
    offers = Offer.objects.all() 
    return render(request, 'offers/offers.html', {
        'offers' : offers
    })

def offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    context = {
        'offer' : offer
    }
    return render(request, 'offers/offer.html', context)
