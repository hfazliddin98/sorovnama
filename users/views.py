from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import KirishForm, RoyhatForm
from baho.models import Turi, Fan


class HomeView(View):
    def get(self, request):
        try:
            fan = Fan.objects.fil(kurs_id=request.user.kurs)
            # data = Turi.objects.filter(fani_id=0)
            print(request.users.kurs)
            # data = fan
        except:
            data = ''


        context = {
            'data':data,
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







