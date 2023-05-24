import Locations
import Agent

import Parameters

   
# Records the moment in which an infection occurs
class infection_event():
    print("inf")    
    def __init__(self, _cur_time = 0):
        self.time = _cur_time
        self.subject = None # Agent the event has occured to
        self.infection_type = "" # CONTACT, AIRBORN, FOOD
        self.infector = None
        self.type = "Infection"
        
    def get_time(self):
        return self.time
    
    def get_type(self):
        return self.type
    
# Records whether starvation or infection killed the subject, 
# holds infection event if infection
class infection_death_event():
    
    def __init__(self):
        self.time = 0
        self.subject = None # Agent the event has occured to
        self.infection_event = None
        self.type = "Infection"
        
    def get_time(self):
        return self.time
    
    def get_type(self):
        return self.type
        
# Records whether starvation or infection killed the subject, 
# holds infection event if infection
class starvation_death_event():
    
    
    def __init__(self):
        self.time = 0
        self.subject = None # Agent the event has occured to
        self.type = "Infection"
        
    def get_time(self):
        return self.time
    
    def get_type(self):
        return self.type