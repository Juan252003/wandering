from turtle import distance
from wandering import ComunWandering
from track import Track
from location import location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, stops):
    begining = location.get_location
    
    for _ in range(stops):
        location.move_wandering(wandering)
        
    return begining.distance(location.get_location(wandering))

def simulate_walk(stops, number_attempts, type_wandering):
    wandering = type_wandering(name='Alirio')
    origen = location(0,0)
    distances = []
    
    for _ in range(number_attempts):
        track = Track()
        track.add_wandering(wandering, origen)
        simulation_walk = walking(track, wandering, stops)
        distances.append(round(simulation_walk, 1))    
    return distances

def graph(x, y):
    graphics = figure(title='Camino del errante', x_axis_label='pasos', y_axis_label='Distancia')
    graphics.line(x, y, legend='Distancias')
    show(graphics)
    


        

        
    
