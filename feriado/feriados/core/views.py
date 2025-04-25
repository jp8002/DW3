from django.shortcuts import render
from datetime import datetime
from core.models import FeriadoModel
from core.service import teste
import ipdb

def feriado(requests):
    hoje = datetime.today()
    qs = FeriadoModel.objects.filter(mes=hoje.month)
    qs = qs.filter(dia=hoje.day)
    # Comentado para evitar erros em uma máquina sem MongoDB
    # teste()
    if len(qs) > 0:
        contexto = {'feriado': True, 'nome':qs[0].nome}
    else:
        contexto = {'feriado': False}
    return render(requests, "feriado.html", contexto)


def listar_feriados(request):
    feriados = FeriadoModel.objects.all().order_by('mes', 'dia')
    return render(request, 'listar_feriados.html', {'feriados': feriados})


from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from core.forms import FeriadoForm, FeriadoForm2

def adicionar_feriado(request):
    if request.method == 'POST':
        form = FeriadoForm(request.POST)
        if form.is_valid():
            FeriadoModel.objects.create(**form.cleaned_data)
            return redirect('listar_feriados')
    else:
        form = FeriadoForm2()
    return render(request, 'adicionar_feriado.html', {'form':form})

def modificar_feriado(request,feriado_id):
    
    feriado = FeriadoModel.objects.filter(id = feriado_id).get()
    
    #ipdb.set_trace()

    
    return render(request, 'modificar_feriado.html', {"feriado" : feriado})

    
    
