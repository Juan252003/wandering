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
    
def main(distances_walk, number_attempts, type_wandering):
    average_walking_distance = []
    
    for stops in distances_walk:
        distances = simulate_walk(stops, number_attempts, type_wandering)
        middle_distances = round(sum(distances) / len(distances), 4)
        max_distances = max(distances)
        min_distances = min(distances)
        average_walking_distance.append(middle_distances)
        print(f'{type_wandering.__name__} Caminata aleatoria de {stops} pasos')
        print(f'Media = {middle_distances}')
        print(f'Max = {max_distances}')
        print(f'Min = {min_distances}')
    graph(distances_walk, average_walking_distance)
    
if __name__ == '__main__':
    
    distances_walk = [10, 100, 1000, 10000]
    number_attempts = 100
    main(distances_walk, number_attempts, ComunWandering)
    
        
        

        
    
