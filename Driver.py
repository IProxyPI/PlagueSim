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

l = Locations.location_parent()

for i in range(1000):
    l.add_agent_to_location(Sim_Tools.create_agent())

a = Sim_Tools.create_agent()
a.infect()

l.add_agent_to_location(a)
event_list = []
time = 0

for i in range(200):
    
    l.update(time)
    time+=1
    output_events = l.attempt_internal_infections()
    for infection in output_events:
        event_list.append(infection)
        
    Visuals.print_data_graphs(event_list, time)
    s = 0
    for a in l.get_agents():
        if a.sick():
            s+=1
    print(s)

# // Runs all tests

#Testing_Module.run_all_tests()