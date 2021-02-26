from django.shortcuts import render, redirect

from .forms import TaskForm


def index(request):
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:index')

    context = {'form': form}
    return render(request, 'tasks/index.html', context)