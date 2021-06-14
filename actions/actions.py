# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa.shared.core.domain import Domain
domain =  Domain.load("domain.yml")
class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        last_intent=tracker.latest_message['intent'].get('name')
        print(last_intent)
        # print(tracker.get_intent_of_latest_message())
        dispatcher.utter_message(response = "utter_faq2/food_help")

        return []

class ActionFaq3(Action):

    def name(self) -> Text:
        return "action_faq3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        last_intent=tracker.latest_message['intent'].get('name')
        print(last_intent)
        print(tracker.latest_message['text']) # to get user typed message 
        print('\n',"New line")

        intent_found = json.dumps(tracker.latest_message['response_selector'][last_intent]['ranking'][0]['intent_response_key'], indent=4)
        #used eval to remove quotes around the string
        
        intent_found = f'utter_{eval(intent_found)}'
        print(intent_found)
        dispatcher.utter_message(response = intent_found) # use response for defining intent name
        # print('All intent ','\n',domain['intents']) # in this way we can get list of all intents
        # dispatcher.utter_message(text= " Ya we are there to help you")

        return []