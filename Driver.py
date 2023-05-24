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



# // Runs all tests

Testing_Module.run_all_tests()