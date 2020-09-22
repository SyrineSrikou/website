from django.contrib import admin

from .models import Offer, Application

class OfferdemandAdmin(admin.ModelAdmin):
    list_display=('offer','name','email','application_date', 'cv', 'message')
    list_display_links = ('offer',)
    list_filter = ('offer',)
    search_fields = ('offer','name','email','application_date',)
    list_per_page = 25
admin.site.register(Offer)
admin.site.register(Application, OfferdemandAdmin)
