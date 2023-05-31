import Agent
import Parameters


import random as rand


class sim_data_manager():
    
    def __init__(self):
    
        self.event_list = []
        self.agent_list = []
        self.location_list = [] # Current unused
        self.state_events = []
        self.sird = [0, 0, 0, 0, 0, 0]
        self.total_infections = 0
        
    def reset_sird(self):
        self.sird = [0, 0, 0, 0, 0, 0]
        
    def get_sird(self):
        return self.sird
    
    def add_s(self):
        self.sird[0] += 1
        
    def add_i(self):
        self.sird[1] += 1
        
    def add_r(self):
        self.sird[2] += 1
        
    def add_d(self):
        self.sird[3] += 1
        
    def add_hi(self):
        self.sird[4] += 1
        
    def add_si(self):
        self.sird[5] += 1
        
    
    
def create_agent( _dm ):
    
    output_agent = Agent.agent()
    
    # Applying randomization from parameters
    
    output_agent.will_stay_home_if_exposed = roll_percentage( Parameters.perc_stay_home_if_sick )
    output_agent.will_stay_home_if_sick = roll_percentage( Parameters.perc_stay_home_if_sick ) or output_agent.will_stay_home_if_exposed
    output_agent.will_mask_if_exposed = roll_percentage( Parameters.perc_mask_if_sick )
    output_agent.will_mask_if_sick = roll_percentage( Parameters.perc_mask_if_sick ) or output_agent.will_mask_if_exposed
    output_agent.will_announce_if_exposed = roll_percentage( Parameters.perc_will_announce_if_sick )
    output_agent.will_announce_if_sick = roll_percentage( Parameters.perc_will_announce_if_sick ) or output_agent.will_announce_if_exposed
    output_agent.washes_hands = roll_percentage( Parameters.perc_washes_hands_if_sick )
    output_agent.washes_hands_when_sick_or_exposed = roll_percentage( Parameters.perc_washes_hands_if_sick ) or output_agent.washes_hands
    output_agent.goes_to_doctor_if_exposed = roll_percentage( Parameters.chance_of_going_to_doctor_if_sick )
    output_agent.goes_to_doctor_if_sick = roll_percentage( Parameters.chance_of_going_to_doctor_if_sick ) or output_agent.goes_to_doctor_if_exposed

    output_agent.anti_isolation = roll_percentage( Parameters.perc_anti_isolation )
    output_agent.anti_mask = roll_percentage( Parameters.perc_anti_mask )
    output_agent.anti_vaccine = roll_percentage( Parameters.perc_anti_vaccine )
     
    output_agent.immune_compromised = roll_percentage( Parameters.perc_immune_compromised )
    output_agent.asymptomatic = roll_percentage( Parameters.perc_asymptomatic )
    
    output_agent.dm = _dm
    output_agent.gen_temp_schedule()
    
    _dm.agent_list.append(output_agent)
    
    return output_agent


def roll_percentage( _perc ):
    return (rand.random() * 100) < _perc

