from django.shortcuts import render
from django.http import HttpResponse
from core.models import FeriadoModel
import datetime 

# Create your views here.

def feriado(request):
    hoje = datetime.datetime.today()
    contexto = {"feriado" : ""}
    
    feriado =  FeriadoModel.objects.filter(dia = hoje.day).filter(mes = hoje.month)
    # import ipdb; ipdb.set_trace()   
    if feriado :
        contexto["feriado"] = feriado[0].nome
    
           
    return render(request, "feriados.html", contexto)



