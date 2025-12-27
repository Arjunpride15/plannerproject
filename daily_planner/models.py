from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Task(models.Model):
    title = models.CharField(max_length=200)
    # Allows storing a description, can be blank
    description = models.TextField(blank=True, null=True)
    # Defaults to the current date when created
    date = models.DateField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        # Orders tasks by completion status (incomplete first), then by date
        ordering = ['is_completed', '-date', '-created_at']
