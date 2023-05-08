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

from Adafruit_IO import RequestError, Client, Feed

ADAFRUIT_IO_USERNAME = 'hungneet'
ADAFRUIT_IO_KEY = 'aio_sAtR88FwrOFXxff2weSfgFK9Gudc'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)



class ActionTellTemp(Action):

    def name(self) -> Text:
        return "action_tell_temp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        temperature_data = aio.receive('sensor2').value
        
        msg = f"The temperature is {temperature_data}°C now."
        dispatcher.utter_message(text=msg)

        return []
    
class ActionTellHumid(Action):

    def name(self) -> Text:
        return "action_tell_humid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        humid_data = aio.receive('sensor1').value
        
        msg = f"The humid is {humid_data}% now."
        dispatcher.utter_message(text=msg)

        return []
    
class ActionLightOn(Action):

    def name(self) -> Text:
        return "action_light_on"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        light_state = aio.receive('button3').value
        print(light_state)
        
        if light_state == '1':
            msg = f"The light is already turn on!"
            dispatcher.utter_message(text=msg)
        else:
            msg = f"Turning on the light!"
            dispatcher.utter_message(text=msg)
            button1_feed = aio.feeds('button3')
            aio.send_data(button1_feed.key, 1)
    
        return []
    
class ActionLightOff(Action):

    def name(self) -> Text:
        return "action_light_off"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        light_state = aio.receive('button3').value
        
        if light_state == '0':
            msg = f"The light is already turn off!"
            dispatcher.utter_message(text=msg)
        else:
            msg = f"Turning off the light!"
            dispatcher.utter_message(text=msg)
            button1_feed = aio.feeds('button3')
            aio.send_data(button1_feed.key, 0)
    
        return []
    
class ActionPumpOn(Action):

    def name(self) -> Text:
        return "action_pump_on"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        pump_state = aio.receive('button1').value
        
        if pump_state == '1':
            msg = f"The pump is already turn on!"
            dispatcher.utter_message(text=msg)
        else:
            msg = f"Starting the pump!"
            dispatcher.utter_message(text=msg)
            button2_feed = aio.feeds('button1')
            aio.send_data(button2_feed.key, 1)
    
        return []
    
class ActionPumpOff(Action):

    def name(self) -> Text:
        return "action_pump_off"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        pump_state = aio.receive('button1').value
        
        if pump_state == '0':
            msg = f"The pump is already turn off!"
            dispatcher.utter_message(text=msg)
        else:
            msg = f"Stopping the pump!"
            dispatcher.utter_message(text=msg)
            button2_feed = aio.feeds('button1')
            aio.send_data(button2_feed.key, 0)
    
        return []
    
    
