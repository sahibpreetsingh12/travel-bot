### Commands for Action server

1. To get Intent of latest message = tracker.get_intent_of_latest_message()

or last_intent=tracker.latest_message['intent'].get('name')

2. To get all slots = print(tracker.slots)

3. To get a particular slot = tracker.get_slot(str(intent_button))

4. To send a  Text responsefrom custom action =  dispatcher.utter_message(text= " Ya we are there to help you")

5. To send a  response from Utter using custom action =  
        dispatcher.utter_message(response = "utter_greet")