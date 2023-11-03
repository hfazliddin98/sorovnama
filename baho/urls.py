from django.urls import path
from .views import GuruhView


urlpatterns = [
    path('', GuruhView.as_view(), name='home') 
]