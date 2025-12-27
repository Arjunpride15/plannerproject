from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
def index(request):
    return render(request, 'daily_planner/index.html')

@login_required
def tasks(request):
    tasks = Task.objects.filter(owner=request.user).order_by('created_at')
    context = {'tasks': tasks}
    return render(request, 'daily_planner/tasks.html', context)

@login_required
def task(request, task_id):
    task = Task.objects.get(id=task_id)
    if not task.owner == request.user:
        raise Http404
    context = {'task': task}
    return render(request, 'daily_planner/task.html', context)

@login_required
def new_task(request):
    """Add a task"""
    if not request.method == "POST":
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('daily_planner:tasks')
    
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, "daily_planner/new_task.html", context)


@login_required
def edit_task(request, task_id):
    """Edit an existing task"""
    task = Task.objects.get(id=task_id)
    if not task.owner == request.user:
        raise Http404
    if not request.method == "POST":
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('daily_planner:tasks')
    context = {"task": task, "form": form}
    return render(request, 'daily_planner/edit_task.html', context)

        