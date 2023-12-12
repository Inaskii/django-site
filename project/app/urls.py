from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('conceitual', views.conceitual , name='conceitual'),
    path('avaliacao', views.avaliacao , name='avaliacao'),
    path('pd', views.pd , name='Pd'),
    path('pp', views.pp , name='pp'),
    path('slide', views.slide , name='slide'),

]