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


@api_view(['POST'])
def XLSXGen(request):
    query = request.data.get('XLSXdata', '')
    arr = query.split(", ")
    if query:
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet(f"КП {datetime.today().strftime('%d.%m.%Y')}")

        logo_url = static('catalog/logo.png')
        logo_url_data = BytesIO(urlopen(f'http://127.0.0.1:8000/{logo_url}').read())
        print(logo_url_data)
        first_merge_format = workbook.add_format({'border': 1, 'bottom_color': 'red'})
        worksheet.merge_range('A1:J1', "", first_merge_format)
        worksheet.set_row(0, 100)
        worksheet.insert_image(0, 0, 'logo', {'image_data': logo_url_data, 'x_scale': 0.7, 'y_scale': 0.7, 'x_offset': 220, 'y_offset': 20})


        second_merge_format = workbook.add_format({'border': 1, 'top_color': 'red'})
        worksheet.merge_range('A2:J2', "", second_merge_format)
        worksheet.set_row(1, 100)



        third_merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter',
                'fg_color': 'yellow'})
        worksheet.merge_range('A3:J3', f"Коммерческое предложение на поставку кухонного оборудования от {datetime.today().strftime('%d.%m.%Y')} г.", third_merge_format)

        forth_row_style = workbook.add_format({'align': 'center', 'bold': 1,})
        worksheet.set_row(3, None, forth_row_style)
        worksheet.write( 3, 0, '№')
        worksheet.write( 3, 1, 'Внешний вид')
        worksheet.write( 3, 2, 'Модель')
        worksheet.write( 3, 3, 'Наименование/описание')
        worksheet.write( 3, 4, 'кВт')
        worksheet.write( 3, 5, 'Габариты, мм.')
        worksheet.write( 3, 6, 'Кол.')
        worksheet.write( 3, 7, 'Цена тг/шт.')
        worksheet.write( 3, 8, 'Итог тг/шт.')
        worksheet.write( 3, 9, 'Сроки')   


        for id,item in  enumerate(arr):

         

            id = id + 4
            product = Product.objects.filter(Q(slug__icontains=item) | Q(name__icontains=item)).values()
            url = product.values_list('image', flat = True)[0]
            name = product.values_list('name',flat = True)[0]
            image_data = BytesIO(urlopen(f'http://127.0.0.1:8000/media/{url}').read())

            number_format = workbook.add_format({'valign': 'vcenter', 'align': 'center',})
            worksheet.write( id, 0, f'{id-3}', number_format)
            worksheet.set_column(0,0, 3)

            worksheet.insert_image(id, 1,'image name', {'image_data': image_data, 'x_scale': 0.1, 'y_scale': 0.1, 'x_offset': 50, 'y_offset': 20})
            worksheet.set_column(1,1, 28)
            worksheet.set_row(id, 100)

            worksheet.write(id, 2, f'{name}')
            
            worksheet.write(id, 3, f'{name}')

        workbook.close()
        output.seek(0)

        filename = 'django_simple.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response
    else:
        raise Http404

