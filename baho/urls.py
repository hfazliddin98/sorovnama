from django.urls import path
from .views import TuriView, OqtuvchiView, BazaView


urlpatterns = [
    path('turi/<str:pk>/', TuriView.as_view(), name='turi'), 
    path('oqtuvchi/<str:fan>/<str:tur>/', OqtuvchiView.as_view(), name='oqtuvchi'),
    path('baza/', BazaView.as_view(), name='baza'), 
]