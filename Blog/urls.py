from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('<int:blogpost_id>', views.blogpost, name='blogpost'),
]