import Agent
import Parameters


import random as rand


class sim_data_manager():
    
    def __init__(self):
    
        self.event_list = []

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
    
    output_agent.immune_compromised = roll_percentage( Parameters.perc_immune_compromised )
    
    
    output_agent.dm = _dm
    output_agent.gen_temp_schedule()
    
    return output_agent


def roll_percentage( _perc ):
    return (rand.random() * 100) < _perc

