from django.shortcuts import render, redirect
from django.views import View
from .form import SorovnomaForm
from .models import Turi, Oqtuvchi


class TuriView(View):
    def get(self, request, pk):
        try:
            data = Turi.objects.filter(fan_id=pk)
        except:
            data = ''

        context = {
            'data':data,
        }
        return render(request, 'baho/turi.html', context)
    
class OqtuvchiView(View):
    def get(self, request, pk):
        try:
            tur = Turi.objects.filter(id=pk)
            kurs = request.user.id
            for t in tur:
                print(t.fan_id)
                print(kurs)
                data = Oqtuvchi.objects.filter(kurs_id=kurs).filter(fan_id=t.fan_id).filter(tur_id=pk)
        except:
            data = ''

        context = {
            'data':data,
        }
        return render(request, 'baho/oqtuvchi.html', context)
    
    def post(self, request, pk):
        form = SorovnomaForm(request.POST)
        if form.is_valid():            
            form.save()
            return redirect('/')
        
        context = {
            'form':form,
        }
        return render(request, 'baho/oqtuvchi.html', context)

    
    
class SorovnomaView(View):
    def get(self, request):
        form = SorovnomaForm()

        context = {
            'form':form,
        }
        return render(request, 'baho/sorovnoma.html', context)

    def post(self, request):
        form = SorovnomaForm(request.POST)
        if form.is_valid():            
            form.save()
            return redirect('/')
        
        context = {
            'form':form,
        }
        return render(request, 'baho/sorovnoma.html', context)