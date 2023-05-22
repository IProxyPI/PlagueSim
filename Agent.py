
# Basic person
class Agent():
    
    def __init__(self):
        
        self.home_location = None
        self.work_location = None
        
        # These parameters determine behavior for when detecting sickness within self,
        # or if sickness is detected and announced by another agent in the same location
        self.will_stay_home_if_sick = False
        self.will_stay_home_if_exposed = False
        self.will_stay_mask_if_sick = False
        self.will_stay_mask_if_exposed = False
        self.will_stay_announce_if_sick = False
        self.will_stay_announce_if_exposed = False
        
        self.exposure_timer = 0 # If exposed, # of hours before exposure/staying home status ends
        
        
        self.is_sick = False
        self.time_sick = 0
        self.food = 24 # if reaches 0, starvation occurs