import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone

from .models import Catastro

#https://xhtml2pdf.readthedocs.io/en/latest/usage.html#using-xhtml2pdf-in-django
def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    #es para cambiar valores de settings.py
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def reporte_all(request):
    template_path = 'cat/html_catastro_formPdf.html'
    #template_path = request
    today = timezone.now()

    catastro = Catastro.objects.all()
    context = {
        'obj': catastro,
        'today': today,
        'request': request
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#recibe el id de la compra
def imprimir_one(request, compra_id):
    
    template_path = 'cat/compras_print_one.html'
    today = timezone.now()

    #filtramos las compras en el modelo    
    enc = Catastro.objects.filter(id=compra_id).first()
    #si existe la compra, cogemos el id vinculada al detalle
    #if enc:
    #detalle = ComprasDet.objects.filter(compra__id=compra_id)
    #else:
    #    detalle={}
    
    context = {
        'detalle': enc,
        #'encabezado':enc,
        'today':today,
        'request': request
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #si pongo attachment se descarga el archivo
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    
    #si pongo inline se descarga el archivo
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    

