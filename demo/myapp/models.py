from django.db import models

# Create your models here.
class TodoItems(models.Model):
    title = models.CharField(max_length=280)
    completed = models.BooleanField(default=False)