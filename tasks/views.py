from django.shortcuts import render

from .forms import TaskForm


def index(request):
    form = TaskForm()

    context = {'form': form}
    return render(request, 'tasks/index.html', context)