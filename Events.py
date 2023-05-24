import Locations
import Agent

import Parameters

class event_parent():
    
    def __init__(self):
        
        self.time = 0
        self.subject = None # Agent the event has occured to
        self.type = "Parent"
    
    def get_time(self):
        return self.time
    
    def get_type(self):
        return self.type
    
# Records the moment in which an infection occurs
class infection_event(event_parent):
    
    def __init__(self):
        self.infection_type = "" # CONTACT, AIRBORN, FOOD
        self.infector = None
        self.type = "Infection"
    
# Records whether starvation or infection killed the subject, 
# holds infection event if infection
class infection_death_event(event_parent):
    
    def __init__(self):
        
        self.relevant_infection_event = None
        self.type = "Infection death"
        
# Records whether starvation or infection killed the subject, 
# holds infection event if infection
class starvation_death_event(event_parent):
    
    def __init__(self):
        
        self.type = "Starvation death"