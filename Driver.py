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
        
        self.dm = Sim_Tools.sim_data_manager()
        self.configured = False
        self.analysis = []
    
    # cities = an array of cities to be used within the simulation
    # sim_time = months to sim
    # print_interval = number of steps inbetween each print
    # live_graph = whether to print the graph at each interval
    def configure(self, cities = [], sim_time = 2, print_interval = -1, live_graph = True):
        self.configured = True
        
        self.sim_time = sim_time
        self.print_interval = print_interval
        self.live_graph = live_graph
        
        self.cities = cities
        
    def run(self):
        
        dm = self.dm
        
        time = 0
        time_until_next_print = self.print_interval
            
        month_range = 12
        
        for i in range(int(self.sim_time * 30 * 24)):
            
            dm.reset_sird()
            
            for city in self.cities:
                place_agents_in_world(time, dm, city.get_locations())
                city.update()
            time+=1
            
            
            cur_state = Events.state_event(time)
            cur_state.set_vals(dm.get_sird())
            dm.event_list.append(cur_state)
            dm.state_events.append(cur_state)

            if (self.print_interval != -1):
                time_until_next_print -= 1
                if (time_until_next_print <= 0):
                    if (self.live_graph):
                        time_until_next_print = self.print_interval
                        Visuals.print_data_graphs(dm.event_list, time, len(dm.agent_list), dm.state_events, True)
                    print_progress_bar(i / (month_range * 30 * 24), 3)
            
            if (cur_state.infected == 0):
                i = int(self.sim_time * 30 * 24)
            
        print("# ---------------------------------------------------------- #")
        print("#                    Simulation complete")
        print("# ---------------------------------------------------------- #")
        # Final Print
        
        self.analysis = analyze_results(dm.event_list, dm.state_events, dm.agent_list)
        
    def print_analysis(self):
        
        Visuals.print_data_graphs(self.dm.event_list, self.sim_time * 30 * 24, len(self.dm.agent_list), self.dm.state_events, False)
        Visuals.print_data_graphs(self.dm.event_list, self.sim_time * 30 * 24, len(self.dm.agent_list), self.dm.state_events, True)
        Visuals.print_stat_analysis(self.analysis)

    def infect_random_agents(self, count):
        infect_random_agents(self.dm, count)
        
    def populate_cities(self):
        for city in self.cities:
            city.populate_city(self.dm)
    
def run_quick_sim_v2( _time = 2, _print_interval = 20):
    
    sim = simulation()
   
    size_factor = 5
   
    c = Locations.city()
    c.add_neighborhood(Locations.generate_neighborhood_set("micro city"))
    for i in range(10*size_factor):
        c.add_neighborhood(Locations.generate_neighborhood_set("residental"))
    for i in range(8*size_factor):
        c.add_neighborhood(Locations.generate_neighborhood_set("business"))
            
    
    sim.configure( cities = [c], sim_time = _time, print_interval = _print_interval, live_graph = True )
    sim.populate_cities()
    sim.infect_random_agents(3)
    
    sim.run()
    sim.print_analysis()
    

def place_agents_in_world(_time, _dm, _locations, _tracker = -1):
    
    for i in range(len(_locations)):
        _locations[i].clear_contents()
    
    agent_list = _dm.agent_list
    
    random.shuffle(agent_list)
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



def print_progress_bar( prog, scale_factor ):
    
    base_size = 40
    
    prog *= base_size * scale_factor
    
    complete = ""
    for i in range(int(prog)):
        complete += "="
    incomplete = ""
    for i in range(int(base_size * scale_factor * 0.5)-int(prog)):
        incomplete += "-"
    
    print("#" + complete + incomplete + "#")

def analyze_results( _list_of_events, _list_of_state_events, _list_of_agents ):
    
    total_infections = 0
    
    for event in _list_of_events:
        if (event.get_type() == "Infection"):
            total_infections += 1   
            
    return [len(_list_of_agents), _list_of_state_events[-1].get_vals()[3], total_infections]
    
run_quick_sim_v2(2, 100)

# // Runs all tests

#Testing_Module.run_all_tests()