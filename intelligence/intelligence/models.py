from django.db import models

class Intelligence(models.Model) : 
    label = models.CharField()
    min_level = models.IntegerField()
    max_level = models.IntegerField()