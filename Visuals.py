import Agent
import Locations
import Parameters
import Events
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def print_data_graphs( _list_of_events, _cur_time, _total_agents, _state_events, accumlative = False ):
    
    _cur_time = int(_cur_time)
    
    susceptable_people = np.full(_cur_time, 0)
    infected_people = np.full(_cur_time, 0)
    dead_people = np.full(_cur_time, 0)
    starved_people = np.full(_cur_time, 0)
    recovered_people = np.full(_cur_time, 0)
    isolating_people = np.full(_cur_time, 0)
    healthy_isolating_people = np.full(_cur_time, 0)
    
    year_marker = np.full(_cur_time, 0)
    hpy = 24 * 30 * 12 # Hours per year
    hpy_factor = 1/12
    for i in range(int((_cur_time)/(hpy*hpy_factor))):
        year_marker[int(hpy_factor*hpy*i)] = _total_agents
    
    if (not accumlative):
        for event in _list_of_events:
            time = event.get_time()-1
    
            if (event.get_type() == "Infection"):
                infected_people[time] += 1
            elif (event.get_type() == "Infection Death"):
                dead_people[time] += 1
            elif (event.get_type() == "Starvation Death"):
                starved_people[time] += 1
            elif (event.get_type() == "Recovered"):
                 recovered_people[time] += 1
                 
        for i in range(int((_cur_time)/(hpy*hpy_factor))):
            year_marker[int(hpy_factor*hpy*i)] = 10
    else:
        for i in range(_cur_time):
            susceptable_people[i] = _state_events[i].get_vals()[0]
            infected_people[i] = _state_events[i].get_vals()[1]
            dead_people[i] = _state_events[i].get_vals()[3]
            #starved_people[i] = _state_events[i].get_vals()[3]
            recovered_people[i] = _state_events[i].get_vals()[2]
            isolating_people[i] = _state_events[i].get_vals()[5] + _state_events[i].get_vals()[4]
            healthy_isolating_people[i] = _state_events[i].get_vals()[4]

            
            
    size_factor = 0.005
    plt.figure().set_figwidth(size_factor * _cur_time)

    plt.ion()  
    
    plt.plot(year_marker, 'k-')
    
    if (accumlative):
        plt.plot(isolating_people, 'c-', label = "Isolating")
        plt.plot(healthy_isolating_people, 'm-', label = "Exposure isolating")
    plt.plot(susceptable_people, 'b-', label = "Susceptable")
    plt.plot(recovered_people, 'g-', label = "Recovered")
    plt.plot(infected_people, 'r-', label = "Infected")
    plt.plot(dead_people, 'k-', label = "Dead")
    #plt.plot(starved_people, 'y-', label = "Starved")
    plt.legend(loc = "upper left")

    plt.show()

def print_stat_analysis( analysis ):
    
    
    
    print("# Total population : " + str(analysis[0]))
    print("# Total deaths : " + str(analysis[1]))
    print("# Total cumulative infections : " + str(analysis[2]))
    print("# ")
    print("# Population percentage dead : " + str(int(1000*(analysis[1]/analysis[0]))/10) + "%")
    print("# Population percentage never infected : " + str(int(1000*(analysis[3]/analysis[0]))/10) + "%")

    

def print_map_data( _list_of_all_locations ):
    pass

