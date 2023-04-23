# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests




class ActionTellTemp(Action):

    def name(self) -> Text:
        return "action_tell_temp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        temperature_url = 'https://io.adafruit.com/api/v2/clowz/feeds/cambien1'
        temp_response = requests.get(temperature_url)
        temp_response_json = temp_response.json()
        
        msg = f"It's {temp_response_json['last_value']} now."
        dispatcher.utter_message(text=msg)

        return []
    
class ActionTellHumid(Action):

    def name(self) -> Text:
        return "action_tell_humid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        humid_url = 'https://io.adafruit.com/api/v2/clowz/feeds/cambien2'
        humid_response = requests.get(humid_url)
        humid_response_json = humid_response.json()
        
        msg = f"It's {humid_response_json['last_value']} now."
        dispatcher.utter_message(text=msg)

        return []
    
class ActionLightOn(Action):

    def name(self) -> Text:
        return "action_light_on"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        button1_url = 'https://io.adafruit.com/api/v2/clowz/feeds/nutnhan1'
        button_response = requests.get(button1_url)
        button_response_json = button_response.json()
        
        light_state = button_response_json['last_value']
        
        if light_state == '1':
            msg = f"The light is already turn on!"
            dispatcher.utter_message(text=msg)
        else:
            msg = f"Turning on the light!"
            dispatcher.utter_message(text=msg)
            button_response_json['last_value'] = '1'
            print(button_response_json)
            r = requests.post(button1_url, data=button_response_json)
            
            print(r.status_code)
            # print(button_response_json)
            
    
        return []
    
class ActionLightOff(Action):

    def name(self) -> Text:
        return "action_light_off"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        button1_url = 'https://io.adafruit.com/api/v2/clowz/feeds/nutnhan1'
        button_response = requests.get(button1_url)
        button_response_json = button_response.json()
        
        light_state = button_response_json['last_value']
        
        if light_state == '0':
            msg = f"The light is already turn off!"
            dispatcher.utter_message(text=msg)
        else:
            msg = f"Turning off the light!"
            dispatcher.utter_message(text=msg)
            requests.put(button1_url, data ={'last_value':'0'})
    
        return []
    
    
