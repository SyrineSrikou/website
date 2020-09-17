from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import PageNotAnInteger, EmptyPage , Paginator

from .models import Offer, Application

def index(request):
    offers = Offer.objects.order_by('-postdate') 

    paginator = Paginator(offers, 4)
    page = request.GET.get('page')
    paged_offerss = paginator.get_page(page)

    context = {
        'offers': paged_offerss  
    }
    return render(request, 'offers/offers.html', context )

def offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    context = {
        'offer' : offer
    }
    return render(request, 'offers/offer.html', context)

def application(request, offer_id):
    if request.method == 'POST' :
        name = request.POST['full_name']
        email = request.POST['email']
        cv = request.FILES['file_cv']
    
        message = request.POST['message']
        offer = get_object_or_404(Offer, pk=offer_id)
        application = Application(name=name, email=email, cv=cv, message=message, offer=offer) 
        application.save()
    return redirect("/")