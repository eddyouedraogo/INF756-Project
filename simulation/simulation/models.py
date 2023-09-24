from django.db import models

class RuleSet(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)


class RuleItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    effect_on_health = models.IntegerField()
    effect_on_mental = models.IntegerField()
    effect_on_intelligence = models.IntegerField()
    ruleSet = models.ForeignKey('RuleSet', on_delete=models.SET_NULL, null=True)