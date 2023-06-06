import random
import math
import time

def read_city_coords(filename):
    city_coords = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split('\t')
            city_id = int(line[0])
            x = float(line[1])
            y = float(line[2])
            city_coords[city_id] = (x, y)

    return city_coords

def calculate_distance(city_coords, path):
    total_distance = 0.0
    num_cities = len(path)

    for i in range(num_cities):
        current_city = path[i]
        next_city = path[(i + 1) % num_cities]

        x1, y1 = city_coords[current_city]
        x2, y2 = city_coords[next_city]

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        total_distance += distance

    return total_distance

def generate_random_path(city_coords):
    num_cities = len(city_coords)
    path = list(range(1, num_cities))  
    random.shuffle(path)  
    path = [1] + path + [1] 

    return path

def nearest_neighbor(city_coords):
    num_cities = len(city_coords)

    visited = [False] * num_cities

    start_city = 1
    visited[start_city - 1] = True

    path = [start_city]

    current_city = start_city
    while len(path) < num_cities:
        min_distance = math.inf
        nearest_city = None

        for city_id, coords in city_coords.items():
            if not visited[city_id - 1]:
                x1, y1 = city_coords[current_city]
                x2, y2 = coords
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

                if distance < min_distance:
                    min_distance = distance
                    nearest_city = city_id

        path.append(nearest_city)
        visited[nearest_city - 1] = True
        current_city = nearest_city

    path.append(start_city)

    distance = calculate_distance(city_coords, path)

    return path, distance


filename = 'TSP.txt'
city_coords = read_city_coords(filename)
path = generate_random_path(city_coords)
path_from_file = [i for i in range(1,101)]
distance = calculate_distance(city_coords, path_from_file)
print(distance)
stime = time.time()
path1, distance1 = nearest_neighbor(city_coords)
print(time.time() - stime)
print(distance1, path1)
