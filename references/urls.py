from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='references'),
    path('<int:reference_id>', views.reference, name='reference'),
]