from django.forms import ModelForm
from .models import Sorovnoma, Baza


class SorovnomaForm(ModelForm):
    class Meta:
        model = Baza
        fields = ['oqtuvchi', 'baho']