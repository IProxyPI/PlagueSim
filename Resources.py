
# Resources that may be moved around the simulation, with current plans thisll
# just be food- can have the contaminated keyword to say if itll cause sickness
# however
class resource_parent():
    
    def __init__(self):
        contaminated = False
        contaminator = None # The person that contaminated this food - For events and tracking