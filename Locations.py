import Agent
import Resources
import Parameters
import Sim_Tools

import random

class location_parent():
    
    def __init__(self):
        
        self.contents = [] # List of all people current within this location
        self.max_capacity = 100000
        self.cur_time = 0
        self.type = "parent"
    
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


class hospital(location_parent):
    
    def __init__(self):
        location_parent.__init__(self)
        self.max_capacity = Parameters.workers_per_hospital
        self.type = "hospital"
        

class house(location_parent):
    
    def __init__(self):
        location_parent.__init__(self)
        self.max_capacity = Parameters.people_per_household
        self.type = "house"

class office(location_parent):
    
    def __init__(self):
        location_parent.__init__(self)
        self.max_capacity = Parameters.workers_per_office
        self.type = "office"

class grocery(location_parent):
    
    def __init__(self):
        location_parent.__init__(self)
        self.max_capacity = Parameters.workers_per_retail
        self.type = "grocery"

class farm(location_parent):
    
    def __init__(self):
        location_parent.__init__(self)
        self.max_capacity = Parameters.workers_per_farm
        self.type = "farm"

class recreation(location_parent):
    
    def __init__(self):
        location_parent.__init__(self)
        self.max_capacity = Parameters.workers_per_recreation
        self.type = "reacreation"



class neighborhood():
    
    def __init__(self):
        
        self.locations = []
    
    def add_location(self, _loc):
        self.locations.append(_loc)
        
    def update(self):
        
        for locs in self.locations:
            locs.update()
            locs.attempt_internal_infections()
    
    def get_all_agents(self):
        
        agent_list = []
        for locs in self.locations:
            agent_list += locs.get_agents()
            
        return agent_list
    
    def get_locations(self):
        return self.locations

    def clear_all_location_agents(self):
        for locs in self.locations:
            locs.clear_contents()
    
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
    
    if (_type == "city"): # Complete miniature city, with all buildings
        return generate_city()
    if (_type == "residental"): # Many houses and recreation
        return generate_residental()
    if (_type == "business"): # Many offices and grocery
        return generate_business()
    if (_type == "hospital"): # Some houses, offices, grocery and hospital
        return generate_hospital()

def populate_neighborhood(_neighborhood, _dm):
    
    workhouse_list = []
    house_list = []
    residents_left = 0
    
    loc = _neighborhood.get_locations()
    
    for i in range(len(loc)):
        if (loc[i].type == "house"):
            house_list.append(loc[i])
        else:
            workhouse_list.append(loc[i])
    
    cur_house = 0
    residents_left = house_list[cur_house].max_capacity
    for i in range(len(workhouse_list)):
        
        cur = workhouse_list[i]
        for j in range(cur.max_capacity):
            
            if (residents_left <= 0):
                cur_house+=1
                residents_left = house_list[cur_house].max_capacity
            
            cur_agent = Sim_Tools.create_agent(_dm)
            cur_agent.work_location = cur
            cur_agent.home_location = house_list[cur_house]
            residents_left -= 1
            
    
def generate_city():
    output_data = neighborhood()
    required_civilians = 0
    factor = 1
    
    for i in range(random.randint(2,7)*factor):
        output_data.add_location(grocery())
        required_civilians += Parameters.workers_per_retail
        
    for i in range(random.randint(1,1)*factor):
        output_data.add_location(hospital())
        required_civilians += Parameters.workers_per_hospital
        
    for i in range(random.randint(1,3)*factor):
        output_data.add_location(office())
        required_civilians += Parameters.workers_per_office
        
    for i in range(random.randint(1,6)*factor):
        output_data.add_location(recreation())
        required_civilians += Parameters.workers_per_recreation
    
    for i in range(round(required_civilians/3)+1):
        output_data.add_location(house())
    
    return output_data
        
def generate_residental():
    pass

def generate_business():
    pass

def generate_hospital():
    pass
