from django.db import models

class TaskState(models.Model):
    name = models.CharField(max_length=100)

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    task_state = models.ForeignKey(TaskState, related_name='tasks', on_delete=models.CASCADE)