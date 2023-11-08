from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import KirishView, RoyhatView, HomeView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('kirish/', KirishView.as_view(), name='kirish'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('royhat/', RoyhatView.as_view(), name='royhat'),     
]