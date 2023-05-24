
# Resources that may be moved around the simulation, with current plans thisll
# just be food- can have the contaminated keyword to say if itll cause sickness
# however
class food_resource():
    
    def __init__(self):
        self.contaminated = False
        self.contaminator = None # The person that contaminated this food - For events and tracking
        self.eaten = False # A check for bug detection
        self.nutrition = 12 # Nutritio restored per food unit
    
    def consume(self):
        
        if (self.eaten):
            
            print("Error, attempting to eat food that is already eaten.")
            a = 3/0
            return 0
        
        self.eaten = True
        return self.nutrition