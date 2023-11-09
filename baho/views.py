import xlwt
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .form import SorovnomaForm
from .models import Umumiy, Oqituvchilar, Sorovnoma, Baza, Fan, Tur, Fanlar, Turlar, Oqituvchi


class TuriView(View):
    def get(self, request, pk):
        try:          
            fan = Fanlar.objects.filter(name=pk)
            for f in fan: 
                fan = pk                            
                data = Tur.objects.filter(kurs=request.user.kurs).filter(fan=f.id).values('name').distinct()
                
        except:
            data = ''
            fan = ''

        context = {
            'data':data,
            'fan':fan,
        }
        return render(request, 'baho/turi.html', context)
    
class OqtuvchiView(View):
    def get(self, request, fan, tur):     
        try:
            tur = Turlar.objects.filter(name=tur)
            fan = Fanlar.objects.filter(name=fan)
            for t in tur:
                for f in fan:

                    print(fan)
                    data = Oqituvchi.objects.filter(kurs=request.user.kurs).filter(fan=f.id).filter(tur=t.id).values('name').distinct()
            
        except:
            data = ''

        context = {
            'data':data,
        }
        return render(request, 'baho/oqtuvchi.html', context)
    
    def post(self, request,fan, pk):
        form = SorovnomaForm(request.POST)
        if form.is_valid():            
            form.save()
            return redirect('/')
        
        context = {
            'form':form,
        }
        return render(request, 'baho/oqtuvchi.html', context)
    

class BazaView(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')

        response['Content-Disposition'] = 'attachment; filename="sorovnoma.xls"'

        wb = xlwt.Workbook(encoding='utf-8')

        ws = wb.add_sheet("sheet1")

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = [
                'Talaba kursi',
                'Fan nomi',
                'Fan turi',
                'Fan o`qtuvchisi',
                'Berilgan baho',                                  
        ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        baza = Baza.objects.all()
        if baza:            
            for my_row in baza:
                row_num = row_num + 1
                ws.write(row_num, 0, my_row.kurs, font_style)
                ws.write(row_num, 1, my_row.fan, font_style)
                ws.write(row_num, 2, my_row.tur, font_style)
                ws.write(row_num, 3, my_row.oqtuvchi, font_style)
                ws.write(row_num, 4, my_row.baho, font_style)           

               
            wb.save(response)
            return response
        
        else:                      
            return HttpResponse('<h1 style="text-center">Malumotlar hali kiritilmagan</h1>')

      

    
