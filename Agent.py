import Parameters
import Resources
import random as rand

# Basic person
class agent():
    
    def __init__(self):
        
        self.home_location = None
        self.work_location = None
        
        # These parameters determine behavior for when detecting sickness within self,
        # or if sickness is detected and announced by another agent in the same location
        self.will_stay_home_if_sick = False
        self.will_stay_home_if_exposed = False
        self.will_mask_if_sick = False
        self.will_mask_if_exposed = False
        self.will_announce_if_sick = False
        self.will_announce_if_exposed = False
        self.washes_hands = False
        self.washes_hands_when_sick_or_exposed = False
        
        self.exposure_timer = 0 # If exposed, # of hours before exposure/staying home status ends
        
        
        self.is_sick = False
        self.time_sick = 0
        self.food = 24 # if reaches 0, starvation occurs
        
        self.immune_compromised = False # If disease = death
        
    def attempt_infect_others(self, _agent_list):
        
        if (self.is_sick):
            
            outgoing_airborne_infection_chance = Parameters.infection_chance
            outgoing_contact_infection_chance = Parameters.infection_chance
            
            if (self.is_masked()):
                outgoing_airborne_infection_chance *= Parameters.mask_infection_reduction
            if (self.will_wash_hands()):
                outgoing_contact_infection_chance *= Parameters.hand_washing_infection_reduction
            
            for cur_agent in _agent_list:
                if (not cur_agent.is_sick):
                    final_airborne = outgoing_airborne_infection_chance
                    final_contact = outgoing_contact_infection_chance
                    
                    if (cur_agent.is_masked()):
                        final_airborne *= Parameters.mask_infection_reduction
                    if (cur_agent.will_wash_hands()):
                        final_contact *= Parameters.hand_washing_infection_reduction
                    
                    if (rand.random() * 100) < (final_airborne * final_contact):
                        cur_agent.infect( self )
                
    # Add infection event here
    def infect(self, infector = None):
        self.is_sick = True
        self.time_sick = 0
        
    def sick(self):
        return self.is_sick
    
    # STUBS HERE
    def is_masked(self):
        return False
    
    def will_wash_hands(self):
        return False