from django.contrib import admin

from .models import Offer, Offerdemand

class OfferdemandAdmin(admin.ModelAdmin):
    list_display=('id','name','email','offer','application_date', 'cv', 'letter')

admin.site.register(Offer)
admin.site.register(Offerdemand, OfferdemandAdmin)
