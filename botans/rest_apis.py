from rest_framework.response import Response
from rest_framework.views import APIView

from .extractor import get_intent_and_food
from .intent import get_answer

class listener(APIView):
    def post(self, request, format=None):
        data = request.data
        inMsg = data["utterance"]

        sit, intent, food = get_intent_and_food(inMsg)

        if(sit != 0):
            if(sit == 1):
                return Response({"ans": "Sorry, I could not understand what you meant. Please make sure you\'re asking me something related to Keto diet. My developers are beginners and are still working on improving me"})

            elif(sit == 2):
                return Response({"ans": "I'm sorry, could you please ask the question again? Also, please make sure you specify the name of the food item or product or the ingredient you\'re looking for"})

        print('Intent: ' + str(intent))
        print('Food: ' + str(food))

        ans = get_answer(intent=intent, food=food)

        return Response({"ans": ans})