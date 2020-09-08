from wit import Wit
from django.conf import settings

def get_intent_and_food(inStr):
    client = Wit(settings.WIT_ACCESS_TOKEN)
    sit = 0

    resp = client.message(inStr)

    try:
        intent = resp['intents'][0]['name']
    except:
        sit = 1
        return sit, '', ''

    try:
        food = resp['entities']['food:food'][0]['body']
    except:
        sit = 2
        return sit, intent, ''

    return sit, intent, food