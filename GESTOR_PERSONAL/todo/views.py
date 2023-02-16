from django.shortcuts import render, redirect
from .models import Todo
from .forms import Todoform
from django.contrib import messages

def index(request):
    tareas= Todo.objects.filter(title__contains=request.GET.get('search', ''))
    context= {'tareas': tareas}

    return render(request, 'todo/index.html', context)

def view(request, id):
    tarea= Todo.objects.get(id=id)
    context= {'tarea': tarea}

    return render(request, 'todo/detail.html', context)

def edit(request, id):
    tarea= Todo.objects.get(id=id)
    if request.method == 'GET':
        form= Todoform(instance= tarea)
    context= {'form': form}

    if request.method == 'POST':
        form= Todoform(request.POST, instance= tarea)
        if form.is_valid():
            form.save()
    context= {'form': form}

    messages.success(request, 'Tarea actualizada correctamente.')
    return render(request, 'todo/edit.html', context)

def create(request):
    if request.method == 'GET':
        form= Todoform()
        context= {'form': form}
    
        return render(request, 'todo/create.html', context)

    if request.method == 'POST':
        form= Todoform(request.POST)
        if form.is_valid():
            form.save()
        context= {'form': form}

        messages.success(request, 'Tarea creada correctamente.')
        return render(request, 'todo/create.html', context)

def delete(request, id):
    tarea= Todo.objects.get(id=id)
    tarea.delete()

    context= {'tarea': tarea}
    return redirect('todo')
