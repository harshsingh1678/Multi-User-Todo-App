from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 300)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title