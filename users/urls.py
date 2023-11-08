from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, KirishView, RoyhatView, home


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', home, name='home'),
    path('kirish/', KirishView.as_view(), name='kirish'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('royhat/', RoyhatView.as_view(), name='royhat'),     
]