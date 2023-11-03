from django.shortcuts import render, redirect
from django.views import View
from .form import GuruhForm


class GuruhView(View):
    def get(self, request):
        form = GuruhForm()

        context = {
            'form':form,
        }
        return render(request, 'baho/baho.html', context)

    def post(self, request):
        form = GuruhForm(request.POST)
        if form.is_valid():
            kurs_id = form.cleaned_data['kurs_id']
            name = form.cleaned_data['name']
            form.save()
            return redirect('/')
        
        context = {
            'form':form,
        }
        return render(request, 'baho/baho.html', context)