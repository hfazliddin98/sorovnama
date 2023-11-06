from django.forms import ModelForm
from .models import Sorovnoma


class SorovnomaForm(ModelForm):
    class Meta:
        model = Sorovnoma
        fields = '__all__'