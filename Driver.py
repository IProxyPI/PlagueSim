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
        
        self.response_threshhold = 40 # % Percentage of population infected for response
        self.respose_effects = [    True,          # Enforce masks
                                    True,          # Enforce vaccine
                                    True       ]   # Enforce isolation
        self.response_deployed = False
        
    # cities = an array of cities to be used within the simulation
    # sim_time = months to sim
    # print_interval = number of steps inbetween each print
    # live_graph = whether to print the graph at each interval
    def configure(self, cities = [], sim_time = 2, print_interval = -1, live_graph = True, track_agent = False):
        self.configured = True
        
        self.sim_time = sim_time
        self.print_interval = print_interval
        self.live_graph = live_graph
        self.tracked_agent = -1
        if (track_agent):
            self.tracked_agent = 1
        
        self.cities = cities
        
    def run(self):
        
        dm = self.dm
        
        time = 0
        time_until_next_print = self.print_interval
            
        month_range = 12
        
        for i in range(int(self.sim_time * 30 * 24)):
            
            if (i == 0.25 * 24 * 30 * 12):
                Parameters.infection_chance *= 7 # Omicron simulation
            
            if (not self.response_deployed and ((dm.get_sird()[1] / len(dm.agent_list) * 100) > self.response_threshhold)):
                self.response_deployed = True
                apply_response(self.respose_effects, dm.agent_list)
            
            dm.reset_sird()
            
            for city in self.cities:
                place_agents_in_world(time, dm, city.get_locations(), self.tracked_agent)
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
                    print_progress_bar(i / (month_range * 30 * 24), 1)
            
            if (cur_state.infected == 0):
                i = int(self.sim_time * 30 * 24)
        Parameters.infection_chance /= 7
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
    
def apply_response( _response_effects, _agent_list ):
    
    vax = _response_effects[1]
    isolate = _response_effects[2]
    mask = _response_effects[0]
    
    for agent in _agent_list:
        
        if (not agent.anti_mask):
            agent.will_always_mask = True
        if (not agent.anti_vaccine):
            agent.vaccinated = True
        if (not agent.anti_isolation):
            agent.will_stay_home_if_exposed = True
            agent.will_stay_home_if_sick = True
    
def run_quick_sim_v2( _time = 2, _print_interval = 20):
    
    sim = simulation()
   
    size_factor = 1
   
    c = Locations.city()
    for i in range(1*size_factor):
        c.add_neighborhood(Locations.generate_neighborhood_set("micro city"))
    for i in range(4*size_factor):
        c.add_neighborhood(Locations.generate_neighborhood_set("residental"))
    for i in range(2*size_factor):
        c.add_neighborhood(Locations.generate_neighborhood_set("business"))
            
    
    sim.configure( cities = [c], sim_time = _time, print_interval = _print_interval, live_graph = True )
    sim.populate_cities()
    sim.infect_random_agents(10)
    
    sim.run()
    sim.print_analysis()
    

def place_agents_in_world(_time, _dm, _locations, _tracker = 1):
    
    for i in range(len(_locations)):
        _locations[i].clear_contents()
    
    agent_list = _dm.agent_list
    
    for i in range(len(agent_list)):
                
        cur = agent_list[i]
        loc = None
        
        schedule = cur.get_schedule()
        cur_action = schedule[_time%24]
        
        if ((cur.is_contagious() and cur.will_stay_home_if_sick and cur.time_sick > Parameters.time_before_symptoms_show * 24) or (cur.is_exposed() and cur.will_stay_home_if_exposed)):
            cur.home_location.add_agent_to_location(cur)
            loc = cur.home_location
            
        elif (cur_action == "sleep"):
            cur.home_location.add_agent_to_location(cur)
            loc = cur.home_location
            
        elif (cur_action == "work" and len(cur.work_location.get_agents()) < cur.work_location.max_capacity and (_time/24)%7 > 2):
            cur.work_location.add_agent_to_location(cur)
            loc = cur.work_location
        else:
            found_loc = False
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
            cur.print_agent(loc)
        
def infect_random_agents(_dm, _num_to_infect):
    
    agent_list = _dm.agent_list
    
    while (_num_to_infect > 0):
        cur = agent_list[random.randint(0,len(agent_list)-1)]
        if (not cur.sick()):
            cur.infect()
            _num_to_infect-=1



def print_progress_bar( prog, scale_factor ):
    
    base_size = 100
    
    prog *= base_size * scale_factor
    
    complete = ""
    for i in range(int(prog)):
        complete += "="
    incomplete = ""
    for i in range(int(base_size * scale_factor)-int(prog)):
        incomplete += "-"
    
    print("#" + complete + incomplete + "#")

def analyze_results( _list_of_events, _list_of_state_events, _list_of_agents ):
    
    total_infections = 0
    uninfected = 0
    
    for event in _list_of_events:
        if (event.get_type() == "Infection"):
            total_infections += 1   
     
    for agent in _list_of_agents:
        if (agent.never_infected):
            uninfected += 1   
           
    return [len(_list_of_agents), _list_of_state_events[-1].get_vals()[3], total_infections, uninfected]

def run_multiple_sims( _sim_count ):
    
    for i in range(_sim_count):
        pass
    
def generate_world( _preset, _size_factor = 2 ):
    c = Locations.city()
    
    
    if (_preset == "Mini city"):
        for i in range(1*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("micro city"))
        for i in range(4*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("residental"))
        for i in range(2*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("business"))
    
    if (_preset == "Large city"):
        for i in range(8*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("micro city"))
        for i in range(12*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("residental"))
        for i in range(8*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("business"))

    if (_preset == "Small town"):
        for i in range(1*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("hospital"))
        for i in range(4*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("residental"))
        for i in range(2*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("recreation"))
    
    if (_preset == "Downtown"):
        for i in range(2*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("micro city"))
        for i in range(12*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("recreation"))
        for i in range(12*_size_factor):
            c.add_neighborhood(Locations.generate_neighborhood_set("business"))
    
    return c    

def check_city_size(_preset):
    c = generate_world(_preset, 1)
    sim = simulation()
    sim.configure( [c] )
    sim.populate_cities()
    return len(sim.dm.agent_list)

def analyze_by_group(_total_infections, _event_list):
    
    unsanitary_infections = 0
    unquarintined_infections = 0
    unannouncer_infections = 0
    asymptomatic_infections = 0

def execute( _sim_args ):
    
    analysis = _sim_args[0]
    response = _sim_args[1]
    sim_time = _sim_args[2]
    print_interval = _sim_args[3]
    world_factor = _sim_args[4]
    world_preset = _sim_args[5]
    sim_count = _sim_args[6]
    
    sim_list = []
    
    for i in range(sim_count):
        
        sim = simulation()
        sim_list.append(sim)
        
        c = generate_world(world_preset, world_factor)
                
        
        sim.configure( cities = [c], sim_time = sim_time, print_interval = print_interval, live_graph = analysis[0], track_agent = analysis[2] )
        sim.populate_cities()
        sim.infect_random_agents(10)
        
        sim.run()
        sim.print_analysis()
    print("# ---------------------------------------------------------- #")
    print("#                    All simulations complete")
    print("# ---------------------------------------------------------- #")
    
    avg_dead_perc = 0
    for sim in sim_list:
        avg_dead_perc += int(1000*(sim.analysis[1]/sim.analysis[0]))/10
    
    print("# Average population percentage dead : " + str(avg_dead_perc/len(sim_list)) + "%")
    
#run_quick_sim_v2(6, 100)

# // Runs all tests

#Testing_Module.run_all_tests()