import xlwt
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .form import SorovnomaForm
from .models import Turi, Oqtuvchi, Sorovnoma, Baza


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

            baza = Sorovnoma.objects.all()
            print(baza)
            return HttpResponse('<h1 style="text-center">Malumot topilmadi</h1>')

      

    
