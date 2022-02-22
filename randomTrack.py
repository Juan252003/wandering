from wandering import ComunWandering
from track import Track
from location import location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, stops):
    begining = location.get_location
    
    for _ in range(stops):
        location.move_wandering(wandering)
        
    return begining.distance(location.get_location(wandering))

        

        
    
