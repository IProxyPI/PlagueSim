from Locations import *
from Agent import *
from Events import *

# Runs all tests
def run_all_tests():
    print("Running all tests.")
    run_minor_tests()
    print("All tests complete.")

# Runs all tests that print no/little return values, consider crashing the failure
# condition for the majority of these tests.
def run_minor_tests():
    print("Running all minor tests.")
    test_location_infection()
    print("Minor tests complete.")
    
# Creates a location, adds agents to the location, and calls the locations infection function
def test_location_infection():
    print("Testing location infection functionality.")
    
    loc = location_parent()
    
    for i in range(20):
        loc.add_agent_to_location(agent())
    
    print(loc.get_agents())
    loc.attempt_internal_infections()
    
    print("Location infection passed.")