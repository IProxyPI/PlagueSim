import Locations
import Agent
import Events
import Testing_Module
import Resources
import Parameters
import Sim_Tools
import Visuals

import random

# Each run of the simulation will be held as a single object- that way, many sims 
# can be run, compared and evaluated seperately without losing the previous as the 
# next starts.
class simulation():
    
    def __init__(self):
        
        self.agent_list = [] # Holds all active agents in this simulation
        self.events_list = [] # Holds all events that occurred over the simulation
        self.location_list = [] # Holds all of the locations

def place_agents_in_world(_time, _dm, _locations, _tracker = -1):
    
    for i in range(len(_locations)):
        _locations[i].clear_contents()
    
    agent_list = _dm.agent_list
    for i in range(len(agent_list)):
        cur = agent_list[i]
        
        schedule = cur.get_schedule()
        cur_action = schedule[_time%24]
        
        if ((cur.is_contagious() and cur.will_stay_home_if_sick and cur.time_sick > Parameters.time_before_symptoms_show * 24) or (cur.is_exposed() and cur.will_stay_home_if_exposed)):
            cur.home_location.add_agent_to_location(cur)
        
        elif (cur_action == "sleep"):
            cur.home_location.add_agent_to_location(cur)
            
            if (_tracker == i):
                print("Agent is sleeping, moved to " + str(cur.home_location))
        elif (cur_action == "work" and len(cur.work_location.get_agents()) < cur.work_location.max_capacity):
            cur.work_location.add_agent_to_location(cur)
            
            if (_tracker == i):
                print("Agent is working, moved to " + str(cur.work_location))
        else:
            found_loc = False
            loc = None
            breaker = 0
            while (found_loc == False):
                loc = _locations[random.randint(0,len(_locations)-1)]
                breaker += 1
                if (not loc.type == "house" and not loc.type == "office" and not loc.type == "farm" and not loc.type == "hospital" and loc.max_capacity > len(loc.get_agents())):
                    found_loc = True
                if (breaker > 10):
                    found_loc = True
                    loc = cur.home_location
            loc.add_agent_to_location(cur)
            
            if (_tracker == i):
                print("Agent is bored, moved to " + str(loc))

def infect_random_agents(_dm, _num_to_infect):
    
    agent_list = _dm.agent_list
    
    while (_num_to_infect > 0):
        cur = agent_list[random.randint(0,len(agent_list)-1)]
        if (not cur.sick()):
            cur.infect()
            _num_to_infect-=1


def run_quick_sim_v2( _print_interval = 4 ):
    
    dm = Sim_Tools.sim_data_manager()
    
    city = Locations.generate_neighborhood_set("city")
    Locations.populate_neighborhood(city, dm)
    infect_random_agents(dm, 3)
    
    total_agents = len(dm.agent_list)
    print(len(dm.agent_list))
    time = 0
    print_interval = _print_interval
    time_until_next_print = print_interval
        
    month_range = 60
    
    for i in range(int(month_range * 30 * 24)):
        
        dm.reset_sird()
        
        place_agents_in_world(time, dm, city.get_locations())
        city.update()
        time+=1
        
        
        cur_state = Events.state_event(time)
        cur_state.set_vals(dm.get_sird())
        dm.event_list.append(cur_state)
        dm.state_events.append(cur_state)


        time_until_next_print -= 1
        if (time_until_next_print <= 0):
            time_until_next_print = print_interval
            Visuals.print_data_graphs(dm.event_list, time, total_agents, dm.state_events, True)
        print(str(i) + " of " + str(month_range * 30 * 24))
    
    
        
    
    # Final Print
    Visuals.print_data_graphs(dm.event_list, time, total_agents, dm.state_events, False)
    Visuals.print_data_graphs(dm.event_list, time, total_agents, dm.state_events, True)
run_quick_sim_v2(50)

# // Runs all tests

#Testing_Module.run_all_tests()