import Locations
import Agent
import Events
import Resources

import Parameters

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
    print("Minor tests complete.")



# Runs all tests that have return values/print status reports, and do not neccesarily
# rely on crashes to show failure conditions. In this case, operation can fail without
# program execution failing
def run_functionality_tests():
    print("Running all functionality tests.")
    test_disease_spread()
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
    
    if (a2.sick()):
        print("Disease spreading between agents passed.")
        test_passed()
    else:
        print("Disease spreading between agents failed.")
        test_failed()
    print()