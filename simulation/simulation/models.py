from django.db import models

class RuleSet(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class RuleItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

class ActionRuleItem(models.Model):
    action = models.IntegerField()
    ruleItem = models.ForeignKey('RuleItem', on_delete=models.CASCADE)
    effect_on_health = models.FloatField()
    effect_on_mental = models.IntegerField()
    effect_on_intelligence = models.IntegerField()
    ruleSet = models.ForeignKey('RuleSet', on_delete=models.SET_NULL, null=True)

class ObjectiveRuleItem(models.Model):
    objective = models.IntegerField()
    ruleItem = models.ForeignKey('RuleItem', on_delete=models.CASCADE)
    effect_on_health = models.IntegerField()
    effect_on_mental = models.IntegerField()
    effect_on_intelligence = models.IntegerField()
    ruleSet = models.ForeignKey('RuleSet', on_delete=models.SET_NULL, null=True)