

# // ------------------------------------------------------
#
#   
#   
#   All definable parameters, presets, or testing configs
#   will be located here in the following sections.
#   
#   
#   
# // ------------------------------------------------------


# // ------------------------------------------------------
#
#                   Disease parameters
#
# // ------------------------------------------------------

infection_chance = 0.005 # % per hour

contagion_period = 7 # Days
infection_period = 14 # Days
time_before_symptoms_show = 3 # Undetectable during this period, unless at hospital
lethality_rate = 5 # % chance of death

# Airborn VS contact is the ratio of infection chance that comes from 
# airborn means, vs direct contact means. These relate to different protection
# types, as well as the chance of contaminating food
airborne_infection_percentage = 50 # % of infection chance that comes from airborne

# This updates automatically
contact_infection_percentage = 100 - airborne_infection_percentage


# // ------------------------------------------------------
#
#                   Protection parameters
#
# // ------------------------------------------------------

# Masks affect airborne infections
mask_infection_reduction = 20 # %. This applies for each mask worn, aka infector and suspectible
# Hand washing affects contact infections
hand_washing_infection_reduction = 20 # %. This applies individually, aka infector and suspectible

vaccine_infection_reduction = 50 # %
vaccine_duration_reduction = 50 # %. How long the sick time is reduced for

# // ------------------------------------------------------
#
#                   Population parameters
#
# // ------------------------------------------------------


# DETERMINING POPULATION WILL BE WEIRD LMAO

# okay so main problem is distributing people around the various
# locations, we'll have to meet about this later, but, itll either be like,
# fill them as we go until we run out of either people or space, or, more likely,
# population is determined by the map/simulated region

# These chances are rolled on every individual to determine their behaviours during
# the simulation
perc_stay_home_if_sick = 20 # %
perc_mask_if_sick = 20 # %
perc_will_announce_if_sick = 20 # %
perc_washes_hands_if_sick = 20 # %

perc_immune_compromised = 2 # %

chance_of_announcing_if_sick = 20 # %
chance_of_going_to_doctor_if_sick = 2 # %

# // ------------------------------------------------------
#
#                   World Response parameters
#
# // ------------------------------------------------------

hospitalizations_to_trigger_lockdown = 20 # %. Percentage of population required to 
# trigger a lockdown, leave at 100 to disable lockdown mechanics
hospitalizations_to_lift_lockdown = 2 # %. Percentage hospitalizations must be under
# to lift lockdown
detections_required_to_start_vaccine = -1 # NO IDEA WHERE TO GET THIS NUMBER LMAO PROBABLY REWORK
vaccine_development_time = 20 # in days

# // ------------------------------------------------------
#
#                   City parameters
#
# // ------------------------------------------------------

random_checkup_chance = 1 # %. Chance a person dedicates a day to go to a hospital for some reason

people_per_household = 3 # Actual US average is 2.5, but unfortuanatly we do not cover half-people in this simulation
workers_per_retail = 9 # Rough data from online
workers_per_recreation = 9 # Assumed same as retail, bad assumption but hey, will fix later
workers_per_hospital = 20 # Unfortuanatly the average of roughly 1000 employees per hospital is too large for this sim
hospital_capacity = workers_per_hospital/4 # To compensate we will consider the average of 4 employees per patient. Over this will overwork a hospital