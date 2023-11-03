import pandas as pd
from django.shortcuts import render
from django.views import View
from .forms import KirishForm


class KirishView(View):

    def get(self, request):
        user = KirishForm()



        context = {
            'user':user,
        }
        return render(request, 'users/kirish.html', context)

    def post(self, request):
        user = KirishForm(request.POST)
        if user.is_valid():
            data = user.cleaned_data
            username = data['username']
            parol = data['parol']
            print(f'{username} va {parol}')
        
        context = {
            'user':user,
        }
        return render(request, 'users/kirish.html', context)







