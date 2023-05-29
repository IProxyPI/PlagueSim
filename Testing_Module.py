import Locations
import Agent
import Events
import Resources
import Parameters
import Sim_Tools
import Visuals

total_tests = 0
passed_tests = 0

def start_test():
    global total_tests
    total_tests += 1

def test_passed():
    global passed_tests
    passed_tests += 1

def test_failed():
    pass

def print_outcome():
    print(str(passed_tests) + " of " + str(total_tests) + " tests passed")

# Runs all tests
def run_all_tests():
    print("Running all tests.")
    run_minor_tests()
    run_functionality_tests()
    print("All tests complete.")
    print_outcome()


# Runs all tests that print no/little return values, consider crashing the failure
# condition for the majority of these tests.
def run_minor_tests():
    print("Running all minor tests.")
    test_location_infection()
    test_visualization()
    print("Minor tests complete.")



# Runs all tests that have return values/print status reports, and do not neccesarily
# rely on crashes to show failure conditions. In this case, operation can fail without
# program execution failing
def run_functionality_tests():
    print("Running all functionality tests.")
    test_disease_spread()
    test_eating_eaten_food()
    test_agent_personality_distribution()
    print("Functionality tests complete.")



# Creates a location, adds agents to the location, and calls the locations infection function
def test_location_infection():
    print()
    print("Testing location infection functionality.")
    
    start_test()
    
    loc = Locations.location_parent()
    
    for i in range(20):
        loc.add_agent_to_location(Agent.agent())
    
    print(loc.get_agents())
    loc.attempt_internal_infections()
    
    test_passed()
    
    print("Location infection passed.")
    print()


# Creates two agents, one of which who is sick. With a 100% infection rate, tests if
# the second agent will get sick after 1 spread.
def test_disease_spread():
    print()
    print("Testing disease spreading between agents.")
    
    start_test()
    
    loc = Locations.location_parent()
    
    a1 = Agent.agent()
    a2 = Agent.agent() 
    
    loc.add_agent_to_location(a1)
    loc.add_agent_to_location(a2)
    
    a1.infect() # make one agent sick
    Parameters.infection_chance = 100 # ensure disease is confirmed to spread
    loc.attempt_internal_infections() # run a spread roll
 
    # create a third agent, make sure disease wont spread with no infection chance
    Parameters.infection_chance = 0 # ensure disease is confirmed to not spread
    a3 = Agent.agent()     
    loc.add_agent_to_location(a3)
    loc.attempt_internal_infections() # run a spread roll
   
 
    if (a2.sick() and not a3.sick()):
        print("Disease spreading between agents passed.")
        test_passed()
    else:
        print("Disease spreading between agents failed.")
        test_failed()
    print()
    
# Eating food that has already been eaten will crash, this uses a try-except
# to continue the tests
def test_eating_eaten_food():
    print()
    print("Testing eating already-eaten food.")
    start_test()
    try:
        f = Resources.food_resource()
        f.consume()
        f.consume()
        print("Testing eating already-eaten food failed.")
        test_failed()
    except:
        print("Testing eating already-eaten food passed.")
        test_passed()
    print()
    
# Confirms that a generated agent actually has the stat distribution defined in parameters,
# checks masking if sick, washing hands normally, and immune compromised
def test_agent_personality_distribution():
    print()
    print("Testing agent personality distribution.")
    start_test()

    total = 500000 

    im_comp = 0
    masker = 0
    hand_washer = 0
    
    for i in range(total):
        a = Sim_Tools.create_agent()
        
        if (a.will_mask_if_exposed):
            masker+=1
        if (a.immune_compromised):
            im_comp+=1
        if (a.washes_hands):
            hand_washer+=1

    print("Results:")
    print("Hand washers: ", str(hand_washer/total), " against goal of ", str(Parameters.perc_washes_hands_if_sick))
    print("Masker: ", str(masker/total), " against goal of ", str(Parameters.perc_mask_if_sick))
    print("Immune compromized: ", str(im_comp/total), " against goal of ", str(Parameters.perc_immune_compromised))
    
    if ( within_tol(hand_washer/total,Parameters.perc_washes_hands_if_sick*0.01,0.005) \
        and within_tol(masker/total,Parameters.perc_mask_if_sick*0.01,0.005) \
        and within_tol(im_comp/total,Parameters.perc_immune_compromised*0.01,0.005) ):
        print("Testing agent personality distribution passed.")
        test_passed()
    else:
        print("Testing agent personality distribution failed.")
        test_failed()
    
    print()

def within_tol( _a, _b, _tol = 0.001 ):
    return abs(_a-_b) < _tol
