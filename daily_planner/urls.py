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
    path('tasks/<int:task_id>/', views.task, name='task')
]