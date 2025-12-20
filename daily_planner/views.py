from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

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
def new_task(request):
    """Add a task"""
    if not request.method == "POST":
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('daily_planner:tasks')
    
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, "daily_planner/new_task.html", context)
    