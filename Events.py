import Locations
import Agent

import Parameters

   
# Records the moment in which an infection occurs
class infection_event():
    
    def __init__(self, _infector, _subject, _cur_time = 0):
        self.time = _cur_time
        self.subject = _subject # Agent the event has occured to
        self.infection_type = "" # CONTACT, AIRBORN, FOOD
        self.infector = _infector
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
        self.healthy_isolation = 0
        self.sick_isolation = 0
        self.type = "State"
        
    def get_time(self):
        return self.time
    
    def get_type(self):
        return self.type

    def set_vals(self, _in):
        self.susceptable = _in[0]
        self.infected = _in[1]
        self.recovered = _in[2]
        self.dead = _in[3]
        self.healthy_isolation = _in[4]
        self.sick_isolation = _in[5]
    
    def get_vals(self):
        return [self.susceptable, self.infected, self.recovered, self.dead, self.healthy_isolation, self.sick_isolation]