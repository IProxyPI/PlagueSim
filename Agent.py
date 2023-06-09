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
        self.will_always_mask = False
        self.will_mask_if_exposed = False
        self.will_announce_if_sick = False
        self.will_announce_if_exposed = False
        self.washes_hands = False
        self.washes_hands_when_sick_or_exposed = False
        self.goes_to_doctor_if_exposed = False
        self.goes_to_doctor_if_sick = False

        self.washes_hands_when_sick_or_exposed = False
        self.goes_to_doctor_if_exposed = False
        self.goes_to_doctor_if_sick = False

        self.asymptomatic = False # Infectious but not otherwise influenced by disease
        self.immune_compromised = False # If disease = death
         
        self.exposure_timer = 0 # If exposed, # of hours before exposure/staying home status ends
        self.immunity_timer = 0 # How long recovery immunity lasts
        
        self.anti_mask = False
        self.anti_vaccine = False
        self.anti_isolation = False
        
        self.vaccinated = False
        
        self.is_sick = False
        self.time_sick = 0
        self.food = 24 # if reaches 0, starvation occurs
        self.recovered = False
        
        self.is_alive = True
        
        self.cur_time = 0
        
        self.never_infected = True
        
        self.times_infected = 0
        self.times_infecting_others = 0
    
    def attempt_infect_others(self, _agent_list):
        
        
        if (self.is_contagious() and self.is_alive):
            
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
                    r = rand.random()
                    if (cur_agent.vaccinated):
                        final_airborne *= (1 - 0.01 * Parameters.vaccine_infection_reduction)
                        final_contact *= (1 - 0.01 * Parameters.vaccine_infection_reduction)
                        
                    if (r < (final_airborne + final_contact)):
                        cur_agent.infect( infector = self )
                        self.times_infecting_others += 1
                if (self.will_announce_if_sick and self.time_sick > Parameters.time_before_symptoms_show * 24 and not self.asymptomatic):
                    cur_agent.exposure_timer = Parameters.time_considered_exposed
                
    # Add infection event here
    def infect(self, infector = None):
        self.is_sick = True
        self.time_sick = 0
        self.never_infected = False
        self.times_infected += 1
        
        self.dm.event_list.append(Events.infection_event(infector, self, self.cur_time))
        self.dm.total_infections += 1
    
    def update(self):
        
        self.cur_time+=1
        self.food -= 1 # Consume one food ## NOT CURRENTLY IMPLEMENTED
        
        if (self.exposure_timer > 0):
            self.exposure_timer -= 1
        
        if (self.recovered and self.is_alive): # Recovery expiring
            self.immunity_timer -= 1
            
            if (self.immunity_timer <= 0):
                self.recovered = False
        
        if (self.is_sick and self.is_alive):
            self.time_sick += 1
            
            v_mod = 1
            if (self.vaccinated):
                v_mod = 1 - 0.01 * Parameters.vaccine_infection_reduction
            
            if (self.time_sick >= Parameters.infection_period * 24):
                if ((rand.random() * 100 <= Parameters.lethality_rate * (v_mod) or self.immune_compromised) and not self.asymptomatic):
                    
                    self.dm.event_list.append(Events.infection_death_event(self.cur_time))
                    self.is_alive = False
                else:
                    self.dm.event_list.append(Events.recovered_event(self.cur_time))
                    self.is_sick = False
                    self.recovered = True
                    self.immunity_timer = Parameters.immunity_period * 24
                    
        self.update_sim_with_state()
    
    def sick(self):
        return self.is_sick
    
    def is_contagious(self):
        return self.is_sick and self.time_sick <= Parameters.contagion_period * 24 and self.time_sick >= 24
    
    def is_exposed(self):
        return self.exposure_timer > 0
    
    def number_of_hours_sick_for(self):
        return self.time_sick
    
    # STUBS HERE
    def is_masked(self):
        return self.will_always_mask or ((self.is_exposed() and self.will_mask_if_exposed) or (self.is_sick and self.will_mask_if_sick))
    
    def will_wash_hands(self):
        return False
    
    def consume_food(self, _food):
        self.food += _food.consume()
    
    def get_schedule(self):
        return self.schedule
    
    def update_sim_with_state(self):
        
        if (not self.is_alive):
            self.dm.add_d()
        elif (self.is_sick):
            self.dm.add_i()
        elif (self.recovered):
            self.dm.add_r()
        else:
            self.dm.add_s()
            
        if (self.is_alive):
            
            if (self.is_exposed() and not self.is_sick and self.will_stay_home_if_exposed) : 
                self.dm.add_hi()
            elif (self.is_sick and self.will_stay_home_if_sick):
                self.dm.add_si()
    
    def print_agent(self, _location ):
        
        status = "Healthy"
        if (not self.is_alive):
            status = "Dead"
        elif (self.is_sick):
            status = "Sick"
        elif (self.immunity_timer > 0):
            status = "Recovering"
        
        print("# ----------------------------------------------- #")
        print("# Agent                 : " + str(self))
        print("# Location              : " + str(_location))
        print("# Status                : " + status)
        print("# ----------------------------------------------- #")
        print("# Masks                 : " + str(self.will_mask_if_exposed))
        print("# Washes handes         : " + str(self.washes_hands))
        print("# Announces if sick     : " + str(self.will_announce_if_sick))
        print("# Stays home if sick    : " + str(self.will_stay_home_if_sick))
        print("# Times sick            : " + str(self.times_infected))
        print("# Times infected others : " + str(self.times_infecting_others))
        print("# Vaccinated            : " + str(self.vaccinated))
        print("# ----------------------------------------------- #")
    
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
                            "free",        #22
                            "sleep"]        #23
        
