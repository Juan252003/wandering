class Track:
    
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    
    def move(self, delta_X, delta_Y):
        return Track(self.x + delta_X, self.y + delta_Y)
    
    def distance(self, other_track):
        delta_X = self.x - other_track.x
        delta_Y = self.y - other_track.y
        
        return (delta_X**2 + delta_Y**2)**0.5
    