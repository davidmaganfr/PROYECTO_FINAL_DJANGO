from django.shortcuts import render
from .models import Contact
from .forms import Contactform
from django.contrib import messages

def index(request):
    contacts= Contact.objects.filter(name__contains=request.GET.get('search', ''))
    context= {'contacts': contacts}

    return render(request, 'agenda/index.html', context)

def view(request, id):
    contact =Contact.objects.get(id=id)
    context = {'contact': contact}

    return render(request, 'agenda/detail.html', context)

def edit(request, id):
    contact= Contact.objects.get(id=id)

    if request.method == 'GET':
        form= Contactform(instance = contact)
        context= {'form': form, 'id': id}

        return render(request, 'agenda/create.html', context)
    
    if request.method == 'POST':
        form= Contactform(request.POST, instance= contact)
        if form.is_valid():
            form.save()
        context= {'form': form, 'id':id}

        messages.success(request, 'Contacto actualizado correctamente.')
        return render(request, 'agenda/create.html', context)
