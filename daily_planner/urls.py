"""Defines URL patterns for the daily_planner project"""


from django.urls import path
from . import views


app_name = 'daily_planner'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all tasks
    path('tasks/', views.tasks, name='tasks'),
    # Detailed page that shows info about a specific task
    path('tasks/<int:task_id>/', views.task, name='task'),
    # Page for adding a task
    path('new_task/', views.new_task, name="new_task"),
    # Page for editing a task
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task')
]