from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import KirishForm, RoyhatForm
from baho.models import Turi, Fan, Sorovnoma, Baza

def home(request): 
        
    try:            
            kursi = request.user.kurs
            data = Fan.objects.filter(kurs_id=request.user.kurs) 
            sorovnoma = Sorovnoma.objects.filter(baza='0')                      
            for s in sorovnoma:
                kurs = s.oqtuvchi_id.kurs_id
                fan = s.oqtuvchi_id.fan_id
                tur = s.oqtuvchi_id.tur_id
                oqtuvchi = s.oqtuvchi_id.name
                baho = s.baho     
                print(s.oqtuvchi_id)            
                
                if s.baza == '1':
                    print('update')                       
                    Baza.objects.update(kurs=kurs, fan=fan, tur=tur, oqtuvchi=oqtuvchi, baho=baho)                        
                else:                    
                    print('create')  
                    Sorovnoma.objects.update(baza='1')                      
                    Baza.objects.create(kurs=kurs, fan=fan, tur=tur, oqtuvchi=oqtuvchi, baho=baho)


    except:
            data = ''
            kursi = ''


    context = {
            'data':data,
            'kurs':kursi,            
    }
    return render(request, 'asosiy/home.html', context)


class HomeView(View):
    def get(self, request):        
        try:            
            kursi = request.user.kurs
            data = Fan.objects.filter(kurs_id=request.user.kurs) 
            sorovnoma = Sorovnoma.objects.filter(baza='0')                      
            for s in sorovnoma:
                kurs = s.oqtuvchi_id.kurs_id
                fan = s.oqtuvchi_id.fan_id
                tur = s.oqtuvchi_id.tur_id
                oqtuvchi = s.oqtuvchi_id.name
                baho = s.baho                
                                
                print('create')  
                Sorovnoma.objects.update(baza='1')                      
                Baza.objects.create(kurs=kurs, fan=fan, tur=tur, oqtuvchi=oqtuvchi, baho=baho)


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
        form = RoyhatForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()          
            return redirect('/kirish/')   
        
        context = {
            'new_user':new_user,
        }
        return render(request, 'users/royhat.html', context)
    








