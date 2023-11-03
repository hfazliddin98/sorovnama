from django import forms


class KirishForm(forms.Form):
    username = forms.CharField(max_length=255)
    parol = forms.CharField(widget=forms.PasswordInput)