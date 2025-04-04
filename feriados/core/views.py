from django.shortcuts import render
from django.http import HttpResponse
import datetime 

# Create your views here.
feriados = {"Natal":"25/12",
            "Canarval":"04/03"}
def natal(request):
    today = datetime.datetime.now().strftime("%d/%m")
    contexo = {"feriado" : ""}
    
    for key, value in feriados.items():
        if (today == value):
            contexo["feriado"] = key
            break
        # import ipdb; ipdb.set_trace()      
    return render(request, "natal.html", contexo)

