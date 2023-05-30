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