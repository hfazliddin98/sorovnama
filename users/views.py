from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import KirishForm, RoyhatForm
from baho.models import Sorovnoma, Baza, Umumiy, Fan, Tur, Oqituvchi




class HomeView(View):
    def get(self, request):        
        try:            
            kursi = request.user.kurs
            data = Fan.objects.filter(kurs=request.user.kurs).values('name').distinct()
            try: 
                fan = Umumiy.objects.filter(baza='0')
                for f in fan:
                    Umumiy.objects.update(baza='1')                    
                    Fan.objects.create(kurs=f.kurs, name=f.fan)
                    Tur.objects.create(kurs=f.kurs, fan=f.fan, name=f.tur)
                    Oqituvchi.objects.create(kurs=f.kurs, fan=f.fan, tur=f.tur, name=f.oqituvchi)                
                
            except:
                print('bajarilmadi')
                
           


        except:
            data = ''
            kursi = ''


        context = {
            'data':data,
            'kurs':kursi,            
        }
        return render(request, 'asosiy/home.html', context)


class KirishView(View):

    def get(self, request):
        form = KirishForm()



        context = {
            'form':form,
        }
        return render(request, 'users/kirish.html', context)

    def post(self, request):
        form = KirishForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Nikname yoki parol xato !!!')
            
        
        context = {
            'form':form,
        }
        return render(request, 'users/kirish.html', context)
    

class RoyhatView(View):

    def get(self, request):
        form = RoyhatForm()



        context = {
            'form':form,
        }
        return render(request, 'users/royhat.html', context)

    def post(self, request):
        new_user = RoyhatForm(request.POST)
        if new_user.is_valid():
            form = new_user.save(commit=False)
            form.set_password(
                new_user.cleaned_data['password']
            )
            form.save()          
            return redirect('/kirish/')         
        
        context = {
            'form':new_user,
        }
        return render(request, 'users/royhat.html', context)
    








