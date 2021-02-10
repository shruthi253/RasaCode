# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

 from typing import Any, Text, Dict, List,Union
 from rasa_sdk import Action, Tracker
 from rasa_sdk.executor import CollectingDispatcher
 from rasa_sdk.forms import FormAction


class InventoryForm(FormAction):

    def name(self) -> Text:
         return "inventory_form"

    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot("confirm_shopping")== True:
            return ["confirm_shopping","item_category","item_name","amount_spent","item_quantity"]
        else:
            return ["confirm_shopping"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: Dict[Text,Any]
    )->List[Dict]:
        return []

    def slot_mappings(self)->Dict[Text,Union[Dict,List[Dict]]]:
        return{
            "confirm_shopping":[
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value= True),
            ],
            "item_category":[
                self.from_entity(entity="category"),
                self.from_intent(intent="deny",value="None"),
            ],
            "item_name":[
                self.from_entity(entity="itemname"),
                self.from_intent(intent="deny",value="None"),
            ],
            "amount_spent":[
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny"),                
            ],
            "item_quantity":[
                self.from_entity(entity="quantity"),
                self.from_intent(intent="deny",value="None"),
            ]

        }


    

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
