import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas
def generate_csv_response(queryset, filename):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']=f'attachment;filename ="{filename}.csv"'
    writer=csv.write(response)
    writer.writerow([field.name for field in queryset.model._meta.fields])
    for obj in queryset :
        writer.writerow([getattr(obj,field.name) for field in queryset.model._meta.fields])
    return response
def generate_pdf_response(queryset,filename):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']=f'attachment;filename="{filename}.pdf"'
    pdf=canvas.Canvas(response)
    y=800
    pdf.setFont("Helvetica-Bold",12)
    pdf.drawstring(100,y,'Student Data')
    pdf.setFont("Helvetica",10)
    y-=20
    for obj in queryset:
        data=f'Name:{obj.name},Event:{obj.event},Selected:{obj.selected}'
        pdf.drawString(100,y,data)
        y-=15
    pdf.showPage()
    pdf.save()
    return response

