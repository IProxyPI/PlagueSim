import Driver

# // ------------------------------------------------------
#
#   
#           User defined simulation parameters
#   
#
#           To configure world/disease parameters, 
#           move to Parameters.py
#   
# // ------------------------------------------------------



# // ------------------------------------------------------
#
#           Execution parameters
#   
# // ------------------------------------------------------

simulation_time = 2 # Months
print_interval = 200 # Time steps between graph/progress bar prints. -1 to disable

world_factor = 2 # Factor to multiply city size by
world_preset = "Small town" # Preset for which city is generated and used in the simulation.

number_of_simulations = 1 # Number of times the simulation is run, results are averaged

#   Available world presets:
#   
#   "Mini city" ~= Population 1601 * world_Factor
#   "Large city" ~= Population 6568 * world_Factor
#   "Small town" ~= Population 866 * world_Factor
#   "Downtown" ~= Population 4942 * world_Factor

# Set true the output/analysis that is desired
analysis_checklist = [     True,       # Display real-time graph
                           False,       # Real-time graph cumulative or not
                           False,       # Track an agent
                           False,
                           False       ]


respose_effects = [    False,          # Enforce masks
                       False,          # Enforce vaccine
                       False       ]   # Enforce isolation
# // ------------------------------------------------------
#
#           Building sim_args
#   
# // ------------------------------------------------------

sim_args = [    analysis_checklist,
                respose_effects,
                simulation_time,
                print_interval,
                world_factor,
                world_preset,
                number_of_simulations   ]

# // ------------------------------------------------------
#   
#           Call to run the simulation
#
# // ------------------------------------------------------

Driver.execute( sim_args )