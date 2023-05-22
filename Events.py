


class event_parent():
    
    def __init__(self):
        
        self.time = 0
        self.day = 0
        self.subject = None # Agent the event has occured to
    

class infection_event(event_parent):
    
    def __init__(self):
        
        self.infector = None
    
# Records whether starvation or infection killed the subject, 
# holds infection event if infection
class death_event(event_parent):
    
    def __init__(self):
        
        self.starvation = False
        self.infection = False
        self.relevant_infection_event = None