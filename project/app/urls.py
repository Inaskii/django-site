from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('conceitual', views.conceitual , name='conceitual'),
    path('avaliacao', views.avaliacao , name='avaliacao'),

]