import Locations
import Agent
import Events
import Testing_Module
import Resources
import Parameters
import Sim_Tools
import Visuals


# Each run of the simulation will be held as a single object- that way, many sims 
# can be run, compared and evaluated seperately without losing the previous as the 
# next starts.
class simulation():
    
    def __init__(self):
        
        self.agent_list = [] # Holds all active agents in this simulation
        self.events_list = [] # Holds all events that occurred over the simulation
        self.location_list = [] # Holds all of the locations


# // Simulation execution functions

def run_quick_sim( _print_interval = 4 ):
    dm = Sim_Tools.sim_data_manager()
    l = Locations.location_parent()
    
    total_agents = 1000
    
    for i in range(total_agents-1):
        l.add_agent_to_location(Sim_Tools.create_agent(dm))
    
    a = Sim_Tools.create_agent(dm)
    a.infect()
    
    l.add_agent_to_location(a)
    time = 1
    
    print_interval = _print_interval
    time_until_next_print = print_interval
    
    for i in range(1000):
        
        l.update()
        time+=1
        output_events = l.attempt_internal_infections()
           
        time_until_next_print -= 1
        if (time_until_next_print <= 0):
            time_until_next_print = print_interval
            Visuals.print_data_graphs(dm.event_list, time, total_agents, True)
    
    # Final Print
    Visuals.print_data_graphs(dm.event_list, time, total_agents, False)
    Visuals.print_data_graphs(dm.event_list, time, total_agents, True)
    a = 0
    for i in l.get_agents():
        if (i.sick()):
            a += 1
    print(a)
run_quick_sim(10)

# // Runs all tests

#Testing_Module.run_all_tests()