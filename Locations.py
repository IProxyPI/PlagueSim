import Agent
import Resources

import Parameters

class location_parent():
    
    def __init__(self):
        
        self.contents = [] # List of all people current within this location
    
    def attempt_internal_infections(self):
        
        for cur_agent in self.contents:
            cur_agent.attempt_infect_others(self.contents)
    
    # For resetting the location of agents
    def clear_contents(self):
        self.contents = []
        
    # Adds the given agent to the current location
    def add_agent_to_location(self, _agent):
        self.contents.append(_agent)
    
    # Returns the list of agents at the location
    def get_agents(self):
        return self.contents