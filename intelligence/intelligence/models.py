from django.db import models

class Intelligence(models.Model) : 
    label = models.CharField(max_length=50)
    min_level = models.IntegerField()
    max_level = models.IntegerField()