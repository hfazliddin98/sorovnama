from django import forms
from .models import User


class KirishForm(forms.Form):
    username = forms.CharField(label='Nikname')
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)

    


class RoyhatForm(forms.ModelForm):
    username = forms.CharField(label='Nikname')
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Parolni takrorlang', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'kurs']
    
    def claen_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Ikkala parol bir biriga teng emas !!!')
        
        return data['password2']
    
  
    