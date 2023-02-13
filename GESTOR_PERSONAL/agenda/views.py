from django.shortcuts import render
from django.http import HttpResponse

def contactos(request):
    return render(request, 'general.html', {})

