from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='offers'),
    path('<int:offer_id>/application', views.application, name='application'),
    path('<int:offer_id>', views.offer, name='offer'),
]