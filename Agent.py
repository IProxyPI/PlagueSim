import Parameters
import Resources
import Events
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
        self.goes_to_doctor_if_exposed = False
        self.goes_to_doctor_if_sick = False
         
        self.immune_compromised = False # If disease = death
         
        self.exposure_timer = 0 # If exposed, # of hours before exposure/staying home status ends
        
        
        self.is_sick = False
        self.time_sick = 0
        self.food = 24 # if reaches 0, starvation occurs
        
        self.cur_time = 0
       
    def attempt_infect_others(self, _agent_list):
        
        infection_events = []
        
        if (self.is_sick):
            
            # Gets basic outgoing chances from this agents parameters
            outgoing_airborne_infection_chance = Parameters.infection_chance * Parameters.airborne_infection_percentage * 0.0001
            outgoing_contact_infection_chance = Parameters.infection_chance * Parameters.contact_infection_percentage * 0.0001
            if (self.is_masked()):
                outgoing_airborne_infection_chance *= Parameters.mask_infection_reduction*0.01
            if (self.will_wash_hands()):
                outgoing_contact_infection_chance *= Parameters.hand_washing_infection_reduction*0.01
            
            # For each agent in the location, get their infection odds, compare them, and roll to see
            # if the agent becomes infected.
            for cur_agent in _agent_list:
                if (not cur_agent.is_sick):
                    
                    final_airborne = outgoing_airborne_infection_chance
                    final_contact = outgoing_contact_infection_chance
                    if (cur_agent.is_masked()):
                        final_airborne *= Parameters.mask_infection_reduction*0.01
                    if (cur_agent.will_wash_hands()):
                        final_contact *= Parameters.hand_washing_infection_reduction*0.01
                    if (rand.random()) < (final_airborne + final_contact):
                        infection_events.append(cur_agent.infect( self ))
        
        
        return infection_events
                
    # Add infection event here
    def infect(self, infector = None):
        self.is_sick = True
        self.time_sick = 0
        
        return Events.infection_event(self.cur_time)
    
    def update(self, _cur_time):
        self.cur_time = _cur_time
    
    def sick(self):
        return self.is_sick
    
    def number_of_hours_sick_for(self):
        return self.time_sick
    
    # STUBS HERE
    def is_masked(self):
        return False
    
    def will_wash_hands(self):
        return False
    
    def consume_food(self, _food):
        self.food += _food.consume()
    
    # This is the main call, manages all stats and whatnot
    def iterate_one_hour(self):
        self.food -= 1 # Consume one food