class Location:
    
    def __init__(self):
        self.location_wandering = {}
    
    def add_wandering(self, wandering, track):
        self.location_wandering[wandering] = track
        
    def move_wandering(self, wandering):
        delta_X, delta_Y = wandering.walk()
        location_now = self.location_wandering[wandering]
        new_location = location_now.move(delta_X, delta_Y)
        
        self.location_wandering[wandering] = new_location
    
    def get_location(self, wandering):
        return self.location_wandering[wandering]
    
    
    
        