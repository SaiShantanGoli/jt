# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import duckling
import datetime
d1 = duckling.Duckling()
d1.load()

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_a_meeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        m_date=tracker.get_slot("date")
        m_time = tracker.get_slot("time")
        
        #output_dict={}

        if not m_date and not m_time:
            dispatcher.utter_message("please provide date and time of meeting")
        elif not m_date:
            dispatcher.utter_message("please provide date of meeting")
        elif not m_time:
            dispatcher.utter_message("please provide time of meeting")
        else:
            output_date=d1.parse(m_date)
            date_from = output_date[-1]['value']['value']
            date_m = str(datetime.datetime.strptime(date_from[0:10],"%Y-%m-%d").date())
            d = datetime.datetime.strptime(date_m,"%Y-%m-%d").strftime("%d/%m/%Y")
     
            output_time=d1.parse(m_time)
            date_f = output_time[-1]['value']['value']
            t = date_f[10:]
            
            #output_dict['date']=d
            #ouptut_dict['startTime']=t

            dispatcher.utter_message("Date and time of meeting is "+d+ " and "+t)

            return [SlotSet('date',None),SlotSet('time',None)]


class ActionJoinMeeting(Action):

    def name(self) -> Text:
        return "action_join_meeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        id_m = tracker.get_slot("meeting_id")

        if not id_m:
            dispatcher.utter_message("please provide meeting id to join the meeting")
        else:
            id_n=id_m[0:3]+'-'+id_m[3:6]+'-'+id_m[6:]
            dispatcher.utter_message('add me into meeting '+id_n)
            return [SlotSet('meeting_id',None)]
