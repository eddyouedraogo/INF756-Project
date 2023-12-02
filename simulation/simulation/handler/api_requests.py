import requests
from rest_framework.response import Response
from ..models import *
from ..serializers import *

def get_labyrinth(data): 
    url = f"http://objects:8100/labyrinth?labyrinth_id={data}"
    result = requests.get(url)

    return handle_http_response(result)


def get_intelligences():
    url = "http://intelligence:8000/intelligence/"
    result = requests.get(url)

    return handle_http_response(result)

def get_action_rule_for_rule_set(rule_set_id):
    rule_set = RuleSet.objects.get(id=rule_set_id);

    data = ActionRuleItem.objects.filter(ruleSet=rule_set).first()

    return ActionRuleItemSerializer(data).data

def get_objective_rule_for_rule_set(rule_set_id):
    rule_set = RuleSet.objects.get(id=rule_set_id);

    data = ObjectiveRuleItem.objects.filter(ruleSet=rule_set)

    return ObjectiveRuleItemSerializer(data, many=True).data


def handle_http_response(result):
    if result.status_code == 200:
        return result.json()
    raise Exception(f"Request returned with code {result.raise_for_status()}")
