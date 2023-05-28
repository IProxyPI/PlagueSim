import Locations
import Agent

import Parameters

   
# Records the moment in which an infection occurs
class infection_event():
    
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
    
    def __init__(self, _cur_time = 0):
        self.time = _cur_time
        self.subject = None # Agent the event has occured to
        self.infection_event = None
        self.type = "Infection Death"
        
    def get_time(self):
        return self.time
    
    def get_type(self):
        return self.type
        
# Records whether starvation or infection killed the subject, 
# holds infection event if infection
class starvation_death_event():
    
    
    def __init__(self, _cur_time = 0):
        self.time = _cur_time
        self.subject = None # Agent the event has occured to
        self.type = "Starvation Death"
        
    def get_time(self):
        return self.time
    
    def get_type(self):
        return self.type
    
class recovered_event():
    
    def __init__(self, _cur_time = 0):
        self.time = _cur_time
        self.subject = None # Agent the event has occured to
        self.infection_event = None
        self.type = "Recovered"
        
    def get_time(self):
        return self.time
    
    def get_type(self):
        return self.type

class state_event():
    
    def __init__(self, _cur_time = 0):
        self.time = _cur_time
        
        self.susceptable = 0
        self.infected = 0
        self.recovered = 0
        self.dead = 0
        
    def get_time(self):
        return self.time
    
    def get_type(self):
        return self.type

    def set_vals(self, _in):
        self.susceptable = _in[0]
        self.infected = _in[1]
        self.recovered = _in[2]
        self.dead = _in[3]
    
    def get_vals(self):
        return [self.susceptable, self.infected, self.recovered, self.dead]