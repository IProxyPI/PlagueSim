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
print_interval = 10 # Time steps between graph/progress bar prints. -1 to disable

world_factor = 2 # Factor to multiply city size by
world_preset = "Large city" # Preset for which city is generated and used in the simulation.

#   Available world presets:
#   
#   "Mini city" ~= Population 1601 * world_Factor
#   "Large city" ~= Population 6568 * world_Factor
#   "Small town" ~= Population 866 * world_Factor
#   "Downtown" ~= Population 4942 * world_Factor

# Set true the output/analysis that is desired
analysis_checklist = [     False,       # Display real-time graph
                           False,       # Real-time graph cumulative or not
                           False,       # Track an agent
                           False,
                           False       ]

# // ------------------------------------------------------
#
#           Building sim_args
#   
# // ------------------------------------------------------

sim_args = []

# // ------------------------------------------------------
#   
#           Call to run the simulation
#
# // ------------------------------------------------------

Driver.execute( sim_args )