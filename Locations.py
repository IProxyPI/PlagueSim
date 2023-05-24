import Agent
import Resources

import Parameters

class location_parent():
    
    def __init__(self):
        
        self.contents = [] # List of all people current within this location
        self.max_capacity = 100000
        self.cur_time = 0;
    
    def attempt_internal_infections(self):
        
       for cur_agent in self.contents:
            cur_agent.update()
            cur_agent.attempt_infect_others(self.contents)


    # For resetting the location of agents
    def clear_contents(self):
        self.contents = []
        
    def update(self):
        self.cur_time += 1
        
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

class neighborhood():
    
    def __init__(self):
        
        self.locations = []
    
    def add_location(self, _loc):
        self.locations.append(_loc)
    
# Current concept: a neighborhood set generates a randomized number of 
# offices, houses, groceries, hospitals and recreation. Order is as follows:
# Houses, hospitals to cover house population, groceries to cover house population,
# recreation to cover house population, offices to cover population - workforce
# required for other services
#
# Agents are not bound to their neighborhood, but may freely roam within a city.
# Just ensures there will be enough locations and facilities per civilian set
#
# Which type of buildings are present is dependant on the neighborhood type
#

def generate_neighborhood_set(_type):
    pass