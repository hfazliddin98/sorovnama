from django.urls import path
from .views import KirishView

urlpatterns = [
    path('', KirishView.as_view(), name='home')    
]