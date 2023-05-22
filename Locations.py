

class location_parent():
    
    def __init__(self):
        
        self.contents = [] # List of all people current within this location
    
    def attempt_internal_infections(self):
        
        for Agent in self.contents:
            pass
            # This is where each infected agent tries to infect a non-infected agent within the location
        