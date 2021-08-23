from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

import json

from django.db.models import Sum
from .models import Catastro
from .forms import CatastroForm, CatastroPDFForm, GDFormPDF
from apps.gdocumental.models import GDocumental

from django.views import generic
from django.urls import reverse_lazy
from apps.bases.views import SinPrivilegios

import reportlab

import io
from django.http import FileResponse, Http404, HttpResponseNotFound
from reportlab.pdfgen import canvas

#fichero pdf
import os
import webbrowser

class CatastroView(generic.ListView):
    model = Catastro
    template_name = "cat/html_catastro_list.html"
    context_object_name = "obj"
    permission_required="apps.catastro.view_catastro"

class CatastroEdit(SuccessMessageMixin,generic.UpdateView):
    model=Catastro
    template_name="cat/html_catastro_form.html"
    context_object_name = 'obj'
    form_class=CatastroForm
    success_url= reverse_lazy("cat:catastro_list")
    success_message="Registro guardado"
    permission_required="apps.catastro.change_catastro"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)

class CatastroNew(SuccessMessageMixin,generic.CreateView):
    model=Catastro
    template_name="cat/html_catastro_form.html"
    context_object_name = 'obj'
    form_class=CatastroForm
    success_url= reverse_lazy("cat:catastro_list")
    success_message="Registro guardado"
    permission_required="apps.catastro.add_catastro"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)

class GestionDocumentalPdf(SuccessMessageMixin,generic.UpdateView):
    model=GDocumental
    #form = GDocumental(id=1)

    template_name="cat/html_catastro_formPdf.html"
    permission_required="apps.catastro.change_catastro"

    context_object_name = 'obj'
    
    #override el modelo
    form_class=GDFormPDF
    #form_class=CatastroPDFForm
    success_url= reverse_lazy("cat:catastro_pdf")
    success_message="Ficheros Adjuntos Catastro"   

    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)

#no funciona
def pdf_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Documento")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='./static_files/pdf/dni.pdf')

#ok, pero descarga
def pdf_view_1(request):
    #with open('./static_files/pdf/dni.pdf', 'r') as pdf:
        #response = HttpResponse(pdf.read(), mimetype='application/pdf')
        #response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        #return response
        #pdf.closed
    try:        
        #static_files/pdf/dni.pdf
        #return FileResponse(open('./static_files/pdf/dni.pdf', 'rb'), content_type='application/pdf')        
        return FileResponse(open('static_files/pdf/dni.pdf', 'rb'), content_type='application/pdf')
        path = 'static_files/pdf/dni.pdf'
        webbrowser.open_new(path)
    except FileNotFoundError:
        raise Http404()

from django.core.files.storage import FileSystemStorage
def pdf_view_2(request):    
    try:                
        fs = FileSystemStorage()
        filename = 'static_files/pdf/dni.pdf'
        if fs.exists(filename):
            with fs.open(filename) as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] ='inline; filename="static_files/pdf/dni.pdf"'
                return response
        else:
            return HttpResponseNotFound('Fichero no encontrado')

        #return FileResponse(open('static_files/pdf/dni.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

# otra forma. no acabada
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        #data = {
        #    'today': datetime.date.today(), 
        #    'amount': 39.99,
        #    'customer_name': 'Cooper Mann',
        #    'order_id': 1233434,
        #}
        pdf = render_to_pdf('cat/pdf.html') #, data)
        return HttpResponse(pdf, content_type='application/pdf')

