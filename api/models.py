from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    