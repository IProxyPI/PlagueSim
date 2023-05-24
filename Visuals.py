import Agent
import Locations
import Parameters
import Events
import numpy as np
import matplotlib.pyplot as plt

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


def print_data_graphs( _list_of_events, _cur_time, _total_agents, accumlative = False ):

    susceptable_people = np.full(_cur_time, _total_agents)
    infected_people = np.full(_cur_time, 0)
    dead_people = np.full(_cur_time, 0)
    starved_people = np.full(_cur_time, 0)
    recovered_people = np.full(_cur_time, 0)

    for event in _list_of_events:
        time = event.get_time()

        if (event.get_type() == "Infection"):
            infected_people[time] += 1
        elif (event.get_type() == "Infection Death"):
            dead_people[time] += 1
        elif (event.get_type() == "Starvation Death"):
            starved_people[time] += 1
        elif (event.get_type() == "Recovered"):
            recovered_people[time] += 1

        if (_cur_time != 0): 
            susceptable_people[time] = susceptable_people[time - 1] - infected_people[time] - dead_people[time]
            - starved_people[time] - recovered_people[time]
        else:
            susceptable_people[time] = _total_agents - infected_people[time] - dead_people[time]
            - starved_people[time] - recovered_people[time]

    plt.plot(susceptable_people, 'b-', label = "Susceptable")
    plt.plot(infected_people, 'r-', label = "Infected")
    #plt.plot(dead_people, 'k-', label = "Dead")
    #plt.plot(starved_people, 'y-', label = "Dead")
    #plt.plot(recovered_people, 'g-', label = "Recovered")
    #plt.legend(loc = "upper left")
    #plt.show()

def print_map_data( _list_of_all_locations ):
    pass