from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def natal(request):
    return HttpResponse("<center><h1>Não é natal.<h1><center>")

