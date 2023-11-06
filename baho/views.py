from django.shortcuts import render, redirect
# from django.views import View
# from .form import GuruhForm, SorovnomaForm


# class GuruhView(View):
#     def get(self, request):
#         form = GuruhForm()

#         context = {
#             'form':form,
#         }
#         return render(request, 'baho/baho.html', context)

#     def post(self, request):
#         form = GuruhForm(request.POST)
#         if form.is_valid():
#             kurs_id = form.cleaned_data['kurs_id']
#             name = form.cleaned_data['name']
#             form.save()
#             return redirect('/')
        
#         context = {
#             'form':form,
#         }
#         return render(request, 'baho/baho.html', context)
    
# class SorovnomaView(View):
#     def get(self, request):
#         form = SorovnomaForm()

#         context = {
#             'form':form,
#         }
#         return render(request, 'baho/sorovnoma.html', context)

#     def post(self, request):
#         form = SorovnomaForm(request.POST)
#         if form.is_valid():            
#             form.save()
#             return redirect('/')
        
#         context = {
#             'form':form,
#         }
#         return render(request, 'baho/sorovnoma.html', context)