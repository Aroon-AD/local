from django.db import models

# Create your models here.
from django.utils import timezone

class TodoList(models.Model):
    title = models.CharField(max_length=250,default = "title")
    content = models.CharField(max_length=250,default = "content")  
    complete = models.BooleanField(default=False)
    status = models.CharField(max_length=25,default = "Incomplete")  
    category = models.CharField(max_length=10,default = "category") 
    created = models.DateField(default=timezone.now())
    due_date = models.DateField(default=timezone.now()) 
    class Meta:
        ordering = ["-created"] 
    def __str__(self):
        return self.title