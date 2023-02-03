import io
from io import BytesIO
import xlsxwriter
from django.http import HttpResponse
from apps.products.models import Product
from urllib.request import urlopen

from django.db.models import Q
from django.http import Http404

from apps.products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

from django.templatetags.static import static


# mainUrl = "127.0.0.1:8000"
mainUrl = "0.0.0.0:8000"

@api_view(['POST'])
def XLSXGen(request):
    query = request.data.get('XLSXdata', '')
    arr = query.split(",")
    res = {}
    for item in arr:
        res[item] = arr.count(item)
    
    
    for id,item in  enumerate(res):
        print(id, item, res[item])
    
    if query:
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'constant_memory': True, 'in_memory': True})
        worksheet = workbook.add_worksheet(f"КП {datetime.today().strftime('%d.%m.%Y')}")
  

        logo_url = static('catalog/logo.png')
        logo_url_data = BytesIO(urlopen(f'http://{mainUrl}{logo_url}').read())
        worksheet.insert_image(0, 0, 'logo', {'image_data': logo_url_data, 'x_scale': 0.7, 'y_scale': 0.7, 'x_offset': 430, 'y_offset': 10})

        first_merge_format = workbook.add_format({'border': 1, 'bottom_color': 'red'})
        worksheet.merge_range('A1:J1', "", first_merge_format)
        worksheet.set_row(0, 70)
        bk_kaz_format = {
            'width': 300,
            'height': 70,
            'y_offset': 10,
            'x_offset': 5,
            'font': {'name': 'Arial',
                    'color': 'black',
                    'size': 12,
                    'bold': True,},
            'align': {'text': 'left',
                    'vertical': 'middle'},
            'border': {'color': 'white'},
            
        }
        worksheet.insert_textbox(0, 0, '"BK Trading Company"\nЖауапкершілігі шектеулі\nсеріктестігі', bk_kaz_format)
        bk_rus_format = {
            'width': 300,
            'height': 70,
            'y_offset': 10,
            'x_offset': 26,
            'font': {'name': 'Arial',
                    'color': 'black',
                    'size': 12,
                    'bold': True,},
            'align': {'text': 'right',
                    'vertical': 'middle'},
            'border': {'color': 'white'},
            
        }
        worksheet.insert_textbox(0, 7, 'Товарищество с ограниченной\nответственностью\n"BK Trading Company"', bk_rus_format)


        second_merge_format = workbook.add_format({'border': 1, 'top_color': 'red'})
        worksheet.merge_range('A2:J2', "", second_merge_format)
        worksheet.set_row(1, 85)
        rek_kaz_format = {
            'width': 300,
            'height': 90,
            'y_offset': 10,
            'x_offset': 5,
            'font': {'name': 'Arial',
                    'color': 'black',
                    'size': 10,
                    'bold': True,},
            'align': {'text': 'left',
                    'vertical': 'middle'},
            'border': {'color': 'white'},
            
        }
        worksheet.insert_textbox(1, 0, 'Қазақстан Республикасы, 020000,\nАлматы қаласы, Алмалы ауданы,\nАуэзов к-сі, 3/5\nБИН: 161 140 000 443\nТел: +7 702 99 777 44\n         +7 778 099 77 44', rek_kaz_format)
        rek_rus_format = {
            'width': 300,
            'height': 90,
            'y_offset': 10,
            'x_offset': 26,
            'font': {'name': 'Arial',
                    'color': 'black',
                    'size': 10,
                    'bold': True,},
            'align': {'text': 'right',
                    'vertical': 'middle'},
            'border': {'color': 'white'},
            
        }
        worksheet.insert_textbox(1, 7, 'Республика Казахстан, 020000,\nг. Алматы, Алмалинский район,\nул. Ауэзова 3/5\nБИН: 161 140 000 443\nТел: +7 702 99 777 44\n+7 778 099 77 44', rek_rus_format)



        third_merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter',
                'font_color': '#244062',
                'font': {
                    'name': 'Arial',
                    'size': 14
                }})
        worksheet.merge_range('A3:J3', f"Коммерческое предложение на поставку кухонного оборудования от {datetime.today().strftime('%d.%m.%Y')} г.", third_merge_format)

        forth_cell_style = workbook.add_format({
                    'align': 'center',
                    'valign': 'vcenter',
                    'border': 1,
                    'bold': 1,
                    'bg_color': '#C4D79B',
                    'font_name': 'Arial', 
                    'size': 10,
            })
        worksheet.set_row(3, 20)
        worksheet.write( 3, 0, '№', forth_cell_style)
        worksheet.write( 3, 1, 'Внешний вид', forth_cell_style)
        worksheet.write( 3, 2, 'Модель', forth_cell_style)
        worksheet.write( 3, 3, 'Наименование/описание', forth_cell_style)
        worksheet.write( 3, 4, 'кВт', forth_cell_style)
        worksheet.write( 3, 5, 'Габариты, мм.', forth_cell_style)
        worksheet.write( 3, 6, 'Кол.', forth_cell_style)
        worksheet.write( 3, 7, 'Цена тг/шт.', forth_cell_style)
        worksheet.write( 3, 8, 'Итог', forth_cell_style)
        worksheet.write( 3, 9, 'Сроки', forth_cell_style)   


        for id,item in  enumerate(res):
            id = id + 4
            product = Product.objects.filter(Q(slug__icontains=item) | Q(name__icontains=item)).values()
           

            number_format = workbook.add_format({'valign': 'vcenter', 'align': 'center','border': 1,})
            worksheet.write( id, 0, (id-3), number_format)
            worksheet.set_column(0,0, 3)

             # IMAGE
            worksheet.set_column(1,1, 25)
            worksheet.set_row(id, 100)
            try:            
                image_cell_format = workbook.add_format({
                    'bold': 1,
                    'align': 'center',
                    'valign': 'vcenter',
                    'border': 1,
                    'font_name': 'Arial',
                    'text_wrap': True,
                    'size': 11})
                url = product.values_list('title_image', flat=True)[0]
                image_data = BytesIO(urlopen(f'http://{mainUrl}/media/{url}').read())
                worksheet.insert_image(id, 1,'image name', {'image_data': image_data, 'x_scale': 0.09, 'y_scale': 0.09, 'x_offset': 30, 'y_offset': 5, 'object_position': 1,})
            except:
                worksheet.write(id, 1, 'Нет данных')

            # NAME
            worksheet.set_column(2,2, 23)
            name_cell_format = workbook.add_format({
                'bold': 1,
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'font_name': 'Arial',
                'text_wrap': True,
                'size': 11})
            try:
                name = product.values_list('name',flat = True)[0]
                worksheet.write(id, 2, f'{name}', name_cell_format)
            except:
                worksheet.write(id, 2, 'Нет данных', name_cell_format)

            # DESCR
            worksheet.set_column(3,3, 30)
            descr_cell_format = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'text_wrap': True,
                'font_name': 'Arial', 
                'size': 11})
            try:
                props = product.values_list('properties',flat = True)[0]
                prop_cell = ''
                for prop in props:
                    prop_cell += "\n" + "\n" + prop
                # descr = product.values_list('description',flat = True)[0]
                worksheet.write(id, 3, f'{prop_cell}', descr_cell_format)
            except:
                worksheet.write(id, 3, 'Нет данных', descr_cell_format)

            # CONSUMPTION
            worksheet.set_column(4,4, 6)
            consumption_cell_format = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'text_wrap': True,
                'font_name': 'Arial', 
                'size': 11})
            try:
                kwt = product.values_list('consumption',flat = True)[0]
                worksheet.write(id, 4, kwt, consumption_cell_format)
            except:
                worksheet.write(id, 4, 'Нет данных', consumption_cell_format)


            # SIZE
            worksheet.set_column(5,5, 18)
            size_cell_format = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'text_wrap': True,
                'font_name': 'Arial', 
                'size': 11})
            try:
                size = product.values_list('dimensions',flat = True)[0]
                worksheet.write(id, 5, f'{size}', size_cell_format)
            except:
                worksheet.write(id, 5, 'Нет данных', size_cell_format)

            # COUNT
            worksheet.set_column(6,6, 6)
            count_cell_format = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'text_wrap': True,
                'font_name': 'Arial', 
                'size': 11})
            try:
                count = res[item]
                worksheet.write(id, 6, count, count_cell_format)
            except:
                worksheet.write(id, 6, 0, count_cell_format)


            # PRICE
            worksheet.set_column(7,7, 15)
            price_cell_format = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'text_wrap': True,
                'num_format': '#,##0 [$₸-kk-KZ]',
                'font_name': 'Arial', 
                'size': 11})
            try:
                price = product.values_list('price',flat = True)[0]
                worksheet.write(id, 7, price, price_cell_format)
            except:
                worksheet.write(id, 7, 0, price_cell_format)

            # PRICE SUM
            worksheet.set_column(8,8, 15)
            sum = price*res[item]
            price_sum_cell_format = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'text_wrap': True,
                'num_format': '#,##0 [$₸-kk-KZ]',
                'font_name': 'Arial', 
                'size': 11})
            worksheet.write(id, 8, sum, price_sum_cell_format)


            worksheet.set_column(9,9, 15)
            ninth_cell_format = workbook.add_format({
                'align': 'center',
                'valign': 'vcenter',
                'border': 1,
                'text_wrap': True,
                'num_format': '#,##0 [$₸-kk-KZ]',
                'font_name': 'Arial', 
                'size': 11})
            worksheet.write(id, 9, f'', ninth_cell_format)

        conclusion_text_style = workbook.add_format({
                    'align': 'center',
                    'valign': 'vcenter',
                    'border': 1,
                    'font_name': 'Arial', 
                    'size': 10,
        })
        conclusion_price_style = workbook.add_format({
                    'align': 'center',
                    'bold': 1,
                    'valign': 'vcenter',
                    'border': 1,
                    'text_wrap': True,
                    'num_format': '#,##0 [$₸-kk-KZ]',
                    'font_name': 'Arial', 
                    'size': 10,
        })
        worksheet.set_row((len(res)+4), 20)
        worksheet.merge_range(f'G{(len(res)+5)}:H{(len(res)+5)}', 'Итого:', conclusion_text_style)
        worksheet.write_formula((len(res)+4), 8, f'=SUM(I5:I{(len(res)+4)})',conclusion_price_style)

        workbook.close()
        output.seek(0)

        filename = f'KP_{datetime.today().strftime("%d.%m.%Y")}.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename={filename}'

        return response
    else:
        raise Http404


