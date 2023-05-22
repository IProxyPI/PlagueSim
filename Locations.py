
class location_parent():
    
    def __init__(self):
        
        self.contents = [] # List of all people current within this location
    
    def attempt_internal_infections(self):
        
        for Agent in self.contents:
            Agent.attempt_infect_others(self.contents)
        