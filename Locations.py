import Agent
import Resources

import Parameters

class location_parent():
    
    def __init__(self):
        
        self.contents = [] # List of all people current within this location
        self.max_capacity = 100000
    
    def attempt_internal_infections(self):
        
        for cur_agent in self.contents:
            cur_agent.attempt_infect_others(self.contents)
    
    # For resetting the location of agents
    def clear_contents(self):
        self.contents = []
        
    def can_add_agent_to_location(self):
        return (len(self.contents) < self.max_capacity)
        
    # Adds the given agent to the current location
    # NOTE, only do this is confirmed by 'can add agent'
    def add_agent_to_location(self, _agent):
        self.contents.append(_agent)
    
    # Returns the list of agents at the location
    def get_agents(self):
        return self.contents
    
    # Gets the capacity of the location
    def get_capacity(self):
        return self.capacity