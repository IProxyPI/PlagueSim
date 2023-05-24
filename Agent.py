import Parameters
import Resources
import Events
import random as rand
import Sim_Tools

# Basic person
class agent():
    
    def __init__(self):
        
        self.home_location = None
        self.work_location = None
        
        self.schedule = []
        
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
        self.recovered = False
        
        self.alive = True
        
        self.cur_time = 0
    
    def attempt_infect_others(self, _agent_list):
        
        
        if (self.is_sick and self.is_contagious()):
            
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
                if (not cur_agent.is_sick and not cur_agent.recovered):
                    
                    final_airborne = outgoing_airborne_infection_chance
                    final_contact = outgoing_contact_infection_chance
                    if (cur_agent.is_masked()):
                        final_airborne *= Parameters.mask_infection_reduction*0.01
                    if (cur_agent.will_wash_hands()):
                        final_contact *= Parameters.hand_washing_infection_reduction*0.01
                    if (rand.random()) < (final_airborne + final_contact):
                        cur_agent.infect( self )
                
    # Add infection event here
    def infect(self, infector = None):
        self.is_sick = True
        self.time_sick = 0
        
        self.dm.event_list.append(Events.infection_event(self.cur_time))
    
    def update(self):
        
        self.cur_time+=1
        self.food -= 1 # Consume one food ## NOT CURRENTLY IMPLEMENTED
        
        if (self.is_sick and self.alive):
            self.time_sick += 1
            
            if (self.time_sick >= Parameters.infection_period * 24):
                if (rand.random() * 100 <= Parameters.lethality_rate):
                    
                    self.dm.event_list.append(Events.infection_death_event(self.cur_time))
                    self.is_alive = False
                else:
                    self.dm.event_list.append(Events.recovered_event(self.cur_time))
                    self.is_sick = False
                    self.recovered = True
    
    def sick(self):
        return self.is_sick
    
    def is_contagious(self):
        return self.is_sick and self.time_sick <= Parameters.contagion_period * 24
    
    def number_of_hours_sick_for(self):
        return self.time_sick
    
    # STUBS HERE
    def is_masked(self):
        return False
    
    def will_wash_hands(self):
        return False
    
    def consume_food(self, _food):
        self.food += _food.consume()
    
    def get_schedule(self):
        return self.schedule
    
    def gen_temp_schedule(self):
        self.schedule = [   "sleep",        #0
                            "sleep",        #1
                            "sleep",        #2
                            "sleep",        #3
                            "sleep",        #4
                            "sleep",        #5
                            "free",        #6
                            "free",        #7
                            "free",        #8
                            "free",        #9
                            "work",        #10
                            "work",        #11
                            "work",        #12
                            "work",        #13
                            "work",        #14
                            "work",        #15
                            "work",        #16
                            "work",        #17
                            "free",        #18
                            "free",        #19
                            "free",        #20
                            "free",        #21
                            "sleep",        #22
                            "sleep"]        #23
