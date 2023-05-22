import Locations
import Agent

from Parameters import *

class event_parent():
    
    def __init__(self):
        
        self.time = 0
        self.day = 0
        self.subject = None # Agent the event has occured to
    
# Records the moment in which an infection occurs
class infection_event(event_parent):
    
    def __init__(self):
        self.infection_type = "" # CONTACT, AIRBORN, FOOD
        self.infector = None
    
# Records whether starvation or infection killed the subject, 
# holds infection event if infection
class death_event(event_parent):
    
    def __init__(self):
        
        self.starvation = False
        self.infection = False
        self.relevant_infection_event = None