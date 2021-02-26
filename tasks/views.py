from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()

    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)

def edit(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')

    context = {'task': task, 'form': form}
    return render(request, 'tasks/edit.html', context)