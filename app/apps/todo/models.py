from django.db import models
 
 
class Todo(models.Model):
    title = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
    def __str__(self) -> str:
        return self.title