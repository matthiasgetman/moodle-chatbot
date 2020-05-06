# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

#class ActionOpenLink(Action):

#	def name(self) -> Text:
#		return "action_open_link"
    
#	def run(self, dispatcher: CollectingDispatcher, 
#			tracker: Tracker,
#			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#		# name = track.get_slot("name")
#		dispatcher.utter_message(text="Opening link now.")
#
#		return []

class PrereqForm(FormAction):
	"""Example of a custom form action"""
	
	def name(self):
		"""Unique identifier of the form"""
		
		return "prereq_form"
	
	@staticmethod	
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""
		
		return ["class_name"]
	
	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "class_name": self.from_entity(entity="class_name", not_intent="deny")
        }
	
	def submit(
		self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
		"""Define what the form has to do after all required slots are filled"""
		
		dispatcher.utter_message(template="utter_did_that_help")
        return []