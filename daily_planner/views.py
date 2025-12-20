from django.shortcuts import render
from .models import Task

def index(request):
    return render(request, 'daily_planner/index.html')
def tasks(request):
    tasks = Task.objects.order_by('created_at')
    context = {'tasks': tasks}
    return render(request, 'daily_planner/tasks.html', context)
def task(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'daily_planner/task.html', context)