from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField()
    date = models.DateField()
    is_finished = models.BooleanField(default=False)
    
class UserTodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    