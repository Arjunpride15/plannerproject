from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "date", "is_completed", "created_at"]
        labels = {'title': "Title: ", "description": "Description: ", "date": "Deadline: ", "is_completed": "Is Completed? ", "created_at": ""}
        widgets = {'description': forms.Textarea(attrs={'cols': 100})}