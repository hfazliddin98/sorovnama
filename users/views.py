import pandas as pd
import requests
from django.shortcuts import render
from django.views import View
from .forms import KirishForm
from .models import Talaba


class KirishView(View):

    def get(self, request):
        form = KirishForm()



        context = {
            'form':form,
        }
        return render(request, 'users/kirish.html', context)

    def post(self, request, requests):
        form = KirishForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            login = data['login']
            parol = data['parol']
            print(f'{login} va {parol}')
            try:
                login_endpoint = "https://talaba.kspi.uz/rest/v1/auth/login"
                payload = {                   
                    "login": '356201103355',
                    "password": "Hfazliddin98"
                }
                req = requests.post(login_endpoint, data=payload)
                data = req.json()
                user_token = data["data"]["token"]

                Talaba.objects.create()


            except:
                pass
        
        context = {
            'form':form,
        }
        return render(request, 'users/kirish.html', context)







