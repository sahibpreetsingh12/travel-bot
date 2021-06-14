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

from rasa_sdk.events import SlotSet
class ActionGreet(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        buttons = [
            {"payload":'/action_faq3{"intent_button":"faq3"}',"title":"faq3"},
            {"payload":'/action_faq3{"intent_button":"faq2"}',"title":"faq2"}
        ]

        dispatcher.utter_message(text="Hi How can i help you with Travel Bot",buttons=buttons)

        return []

class ActionFaq3(Action):

    def name(self) -> Text:
        return "action_faq3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # to get a slot value (here --> slot is intent_button)
        print("slots value is ",tracker.slots['intent_button']) 
        slot_value_clicked = tracker.slots['intent_button']

        # to get intent of user message
        _intent=tracker.latest_message['intent'].get('name')
        print("Intent of user message ",_intent)

        print(tracker.latest_message['text']) # to get user typed message 

        # actual retrieval intent found
        intent_found = json.dumps(tracker.latest_message['response_selector'][_intent]['ranking'][0]['intent_response_key'], indent=4)
        if _intent==slot_value_clicked[0]:
        #used eval to remove quotes around the string
            intent_found = f'utter_{eval(intent_found)}'
            
            dispatcher.utter_message(response = intent_found) # use response for defining intent name
        else:
             dispatcher.utter_message(text = f"Please select your questions from {slot_value_clicked}")

        return []