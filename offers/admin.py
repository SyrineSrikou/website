from django.contrib import admin

from .models import Offer, Application

class OfferdemandAdmin(admin.ModelAdmin):
    list_display=('offer','name','email','application_date', 'cv', 'message')

admin.site.register(Offer)
admin.site.register(Application, OfferdemandAdmin)
