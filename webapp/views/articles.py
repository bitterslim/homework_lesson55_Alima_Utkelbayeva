from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.form import TaskForm
from webapp.models import Task


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    task_data = {
        'title': request.POST.get('title'),
        'status': request.POST.get('status', 'new'),
        'date': request.POST.get('date', None),
        'description': request.POST.get('description', None)
    }
    task = Task.objects.create(**task_data)
    return redirect('task_detail', pk= task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task.html', context=context)


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_update.html', context={'task': task})
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.status = request.POST.get('status', 'new')
        task.description = request.POST.get('description')
        task.date = request.POST.get('date')
        task.save()
        return redirect('task_detail', pk=pk)
    return render(request, 'task_update.html', context={'task': task})

def task_delete_view(request, pk):

    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':

       return render(request, 'task_delete.html', context={'task': task})

    elif request.method == 'POST':

        task.delete()

        return redirect('index')



