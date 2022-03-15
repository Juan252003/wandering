import random

class wandering:
        
    def __init__(self, name, x=0, y=0):
        
        self.name = name
        self.x = x
        self.y = y
        
    def posicion(self):
        return (self.x, self.y)
    
    def distance_origin(self):
        return (self.x**2 + self.y**2)**0.5
              
class ComunWandering(wandering):
    
    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        dx, dy = random.choice([(0,2), (0,-2), (2,0), (-2,0)])
        self.x += dx
        self.y += dy
        return [dx, dy]

class RightWandering(wandering):
    
    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        dx, dy = random.choice([(8,0), (4,0), (2,0), (2,0)])
        self.x += dx
        self.y += dy
        return [dx, dy]

class leftWandering(wandering):
    
    def __init__(self, name):
        super().__init__(name)
        
    def walk(self):
        dx, dy = random.choice([(-8,0), (-4,0), (-2,0), (-2,0)])
        self.x += dx
        self.y += dy
        return [dx, dy]