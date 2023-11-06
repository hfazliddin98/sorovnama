from django.urls import path
from .views import TuriView, OqtuvchiView, SorovnomaView


urlpatterns = [
    path('turi/<int:pk>/', TuriView.as_view(), name='turi'), 
    path('oqtuvchi/<int:pk>/', OqtuvchiView.as_view(), name='oqtuvchi'),
    path('sorovnoma/', SorovnomaView.as_view(), name='sorovnoma'),
]