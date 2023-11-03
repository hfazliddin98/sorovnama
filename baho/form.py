from django.forms import ModelForm
from .models import Guruh

class GuruhForm(ModelForm):
    class Meta:
        model = Guruh
        fields = ["kurs_id", "name"]