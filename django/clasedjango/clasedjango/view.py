from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludos(requets, edad):
    
    document_Exte= open("D:/ESTUDIOS/Coomeva/Desarrollo de Backend/Clases/2020-09-23/django/clasedjango/clasedjango/plantillas/index.html")
    plt = Template(document_Exte.read())
    document_Exte.close()
    ctx = Context({'edad':edad})
    document = plt.render(ctx)
    return HttpResponse(document)

def login(requets):
    return HttpResponse('Bienvenido')
    