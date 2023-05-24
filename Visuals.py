import Agent
import Locations
import Parameters
import Events
import numpy as np

#   NOTES:
#   Locations have a capacity, and list of agents within the location.
#   Agents hold within themselves all data relating to their current state.
#
#   Access:
#
#   loc = Locations.house()
#   OR (for loc in _list_of_all_locations)
#
#   loc.get_agents(self): Returns all agents at this house
#
#   loc.get_capacity(self): Returns the capacity of the house for drawing
#
#   agent = Agent.agent()
#   OR (for agent in _list_of_all_agents)
#
#   agent.sick(self): Returns if this agent is currently sick


def print_data_graphs( _list_of_events, _cur_time ):
    
    
    infected_people = np.full(_cur_time, 0)
    for event in _list_of_events:
        if (event.get_type() == "Infection"):
            infected_people[event.get_time()] += 1

def print_map_data( _list_of_all_locations ):
    pass