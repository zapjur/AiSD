import numpy as np
import random
import math
import matplotlib.pyplot as plt
import time

def read_data_from_file(file_path):
    items = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()[2:]
        
        for line in lines:
            line = line.strip()
            item_data = line.split(',')
            item = {
                'id': int(item_data[0]),
                'width': int(item_data[1]),
                'height': int(item_data[2]),
                'value': int(item_data[3])
            }
            items.append(item)
    
    return items

def backpack_greedy(packages, capacity):
    backpack = np.zeros((capacity, capacity))
    sorted_packages = sorted(packages, key=lambda x: x['value']/(x['height'] * x['width']), reverse = True)
    for item in sorted_packages:
        item_id = item['id']
        item_width = item['width']
        item_height = item['height']
        item_value = item['value']
        inserted = False
        
        if not inserted:
            for w in range(capacity - item_width +1):
                if w + item_width > capacity +1:
                    break
                for h in range(capacity - item_height +1):
                    if h + item_height > capacity +1:
                        break

                    if np.all(backpack[w: w + item_width, h: h + item_height] == 0):
                        backpack[w: w + item_width, h: h + item_height] = item_id
                        inserted = True
                        break
                if inserted:
                    break
                    
        if not inserted:
            item_width, item_height = item_height, item_width
            for w in range(capacity - item_width +1):
                if w + item_width > capacity +1:
                    break
                for h in range(capacity - item_height +1):
                    if  + item_height > capacity +1:
                        break

                    if np.all(backpack[w: w + item_width, h: h + item_height] == 0):
                        backpack[w: w + item_width, h: h + item_height] = item_id
                        inserted = True
                        break
                if inserted:
                    break
                    
    value = evaluate_solution(backpack, packages)

    return backpack, value

#------------------------------------------------

def initialize_solution(capacity):
    return np.zeros((capacity, capacity))

def generate_initial_solution(packages, capacity):
    solution = initialize_solution(capacity)
    random.shuffle(packages)
    
    for item in packages:
        item_id = item['id']
        item_width = item['width']
        item_height = item['height']
        inserted = False
        
        if not inserted:
            for w in range(capacity - item_width +1):
                if w + item_width > capacity +1:
                    break
                for h in range(capacity - item_height +1):
                    if h + item_height > capacity +1:
                        break

                    if np.all(solution[w: w + item_width, h: h + item_height] == 0):
                        solution[w: w + item_width, h: h + item_height] = item_id
                        inserted = True
                        break
                if inserted:
                    break
                    
        if not inserted:
            item_width, item_height = item_height, item_width
            for w in range(capacity - item_width +1):
                if w + item_width > capacity +1:
                    break
                for h in range(capacity - item_height +1):
                    if  + item_height > capacity +1:
                        break

                    if np.all(solution[w: w + item_width, h: h + item_height] == 0):
                        solution[w: w + item_width, h: h + item_height] = item_id
                        inserted = True
                        break
                if inserted:
                    break
    
    return solution

def evaluate_solution(solution, packages):
    total_value = 0
    counted_ids = set()
    
    for row in solution:
        for item_id in row:
            if item_id != 0 and item_id not in counted_ids:
                counted_ids.add(item_id)
                item = next((item for item in packages if item['id'] == item_id), None)
                if item:
                    total_value += item['value']
    
    return total_value

def sort_key(id_, packages):
    item = next(item for item in packages if item['id'] == id_)
    return item['value'] / (item['width'] * item['height'])

def filling_for_neighbor(solution, packages, capacity):
    sorted_packages = sorted(packages, key=lambda x: x['value']/(x['height'] * x['width']), reverse = True)
    for item in sorted_packages:
        item_id = item['id']
        item_width = item['width']
        item_height = item['height']
        item_value = item['value']
        inserted = False
        if not np.isin(item_id, solution):
            for w in range(capacity - item_width +1):
                for h in range(capacity - item_height +1):

                    if np.all(solution[w: w + item_width, h: h + item_height] == 0):
                        solution[w: w + item_width, h: h + item_height] = item_id
                        inserted = True
                        return solution, inserted
                    
            if not inserted:
                item_width, item_height = item_height, item_width
                for w in range(capacity - item_width +1):
                    for h in range(capacity - item_height +1):

                        if np.all(solution[w: w + item_width, h: h + item_height] == 0):
                            solution[w: w + item_width, h: h + item_height] = item_id
                            inserted = True
                            return solution, inserted
    return solution, inserted

def neighbor(curr_solution, packages, capacity):

    #wstępna próba włozenia
    solution, inserted = filling_for_neighbor(curr_solution, packages, capacity)
    if inserted:
        return solution
    #robienie listy z id występującymi w macierzy
    list_id = []
    for w in range(len(curr_solution)):
        for h in range(len(curr_solution)):
            if curr_solution[w, h] != 0 and not np.isin(curr_solution[w, h], list_id):
                list_id.append(curr_solution[w, h])

    #próba poukładania przedmiotów inaczej
    solution = np.zeros_like(curr_solution)
    inserted_counter = 0
    random.shuffle(list_id)
    for id in list_id:
        item = next((item for item in packages if item['id'] == id), None)
        item_id = item['id']
        item_width = item['width']
        item_height = item['height']
        inserted = False

        for w in range(capacity - item_width +1):
            for h in range(capacity - item_height +1):

                if np.all(solution[w: w + item_width, h: h + item_height] == 0):
                    solution[w: w + item_width, h: h + item_height] = item_id
                    inserted = True
                    inserted_counter += 1
                    break
            if inserted:
                break
                    
        if not inserted:
            item_width, item_height = item_height, item_width
            for w in range(capacity - item_width +1):
                for h in range(capacity - item_height +1):

                    if np.all(solution[w: w + item_width, h: h + item_height] == 0):
                        solution[w: w + item_width, h: h + item_height] = item_id
                        inserted = True
                        inserted_counter += 1
                        break
                if inserted:
                    break
    
    if len(list_id) == inserted_counter:
        solution, inserted = filling_for_neighbor(solution, packages, capacity)
    if inserted:
        return solution

    #wstawianie zer za przedmiot o najgorszym ratio
    list_id = sorted(list_id, key=lambda id_, packages=packages: sort_key(id_, packages))
    item = next((item for item in packages if item['id'] == list_id[0]), None)
    item_id = item['id']
    item_width = item['width']
    item_height = item['height']
    solution = np.copy(curr_solution)
    if np.isin(item_id, solution):
        for w in range(len(solution)):
            for h in range(len(solution)):
                if solution[w, h] == item_id:
                    solution[w, h] = 0

    #wkladanie czegos zamiast wyzerowanego elementu
    solution, inserted = filling_for_neighbor(solution, packages, capacity)
    if inserted:
        return solution

    return curr_solution

def acceptance_probability(old_value, new_value, temperature):
    if new_value > old_value:
        return 1.0
    return math.exp((new_value - old_value) / temperature)

def filling(solution, packages, capacity):
    sorted_packages = sorted(packages, key=lambda x: x['value']/(x['height'] * x['width']), reverse = True)
    for item in sorted_packages:
        item_id = item['id']
        item_width = item['width']
        item_height = item['height']
        item_value = item['value']
        inserted = False
        if not np.isin(item_id, solution):
            for w in range(capacity - item_width +1):
                for h in range(capacity - item_height +1):

                    if np.all(solution[w: w + item_width, h: h + item_height] == 0):
                        solution[w: w + item_width, h: h + item_height] = item_id
                        inserted = True
                        break
                if inserted:
                    break
                    
            if not inserted:
                item_width, item_height = item_height, item_width
                for w in range(capacity - item_width +1):
                    for h in range(capacity - item_height +1):

                        if np.all(solution[w: w + item_width, h: h + item_height] == 0):
                            solution[w: w + item_width, h: h + item_height] = item_id
                            inserted = True
                            break
                    if inserted:
                        break
    return solution

def simulated_annealing(packages, capacity):
    temperature = 10000
    cooling_rate = 0.01
    current_solution = generate_initial_solution(packages, capacity)
    best_solution = np.copy(current_solution)
    best_value = evaluate_solution(best_solution, packages)
    alltime_best = np.copy(current_solution)
    alltime_best_value = best_value
    iteration_values = []

    while temperature > 0.1:
        new_solution = neighbor(current_solution, packages, capacity)
        new_value = evaluate_solution(new_solution, packages)
        
        if acceptance_probability(best_value, new_value, temperature) > random.random():
            current_solution = new_solution
            best_solution = np.copy(current_solution)
            best_value = new_value
            if best_value > alltime_best_value:
                alltime_best_value = best_value
                alltime_best = np.copy(best_solution)
        
        temperature *= 1 - cooling_rate
        iteration_values.append(best_value)

    best_solution = filling(best_solution, packages, capacity)
    alltime_best = filling(alltime_best, packages, capacity)
    alltime_best_value = evaluate_solution(alltime_best, packages)
    best_value = evaluate_solution(best_solution, packages)
    if best_value > alltime_best_value:
        alltime_best = best_solution
        alltime_best_value = best_value

    return alltime_best, alltime_best_value, iteration_values

def display_backpack(backpack, title):
    fig, ax = plt.subplots()
    im = ax.matshow(backpack, cmap='viridis')

    for i in range(len(backpack)):
        for j in range(len(backpack[i])):
            ax.text(j, i, f'{backpack[i][j]:.0f}', ha='center', va='center', color='black', fontsize=6)

    plt.colorbar(im)
    plt.title(title)
    plt.show()

def check_time(packages, capacity):
    stime = time.time()
    sim_bp, sim_val, iter = simulated_annealing(packages, capacity)
    time_sim = time.time() - stime
    stime = time.time()
    backpack, value = backpack_greedy(packages, capacity)
    time_greedy = time.time() - stime
    print(f"Greedy alg time: {time_greedy}, value: {value}")
    print(f"Simulated Annealing alg time: {time_sim}, value: {sim_val}")

def display_plot_iter_val(iteration_values):
    plt.plot(range(len(iteration_values)), iteration_values)
    plt.xlabel('Iterations')
    plt.ylabel('Value')
    plt.title('Iterations to Values')
    plt.show()

def main():
    packages20path = 'packages/packages20.txt'
    packages100path = 'packages/packages100.txt'
    packages500path = 'packages/packages500.txt'
    packages1000path = 'packages/packages1000.txt'

    packages = read_data_from_file(packages20path)
    capacity = 20
    greedy_bp, greedy_val = backpack_greedy(packages, capacity)
    sim_bp, sim_val, iteration_values = simulated_annealing(packages, capacity)
    for i in range(10):
        bp, val, iter_val = simulated_annealing(packages, capacity)
        if val > sim_val:
            sim_val = val
            sim_bp = bp
            iteration_values = iter_val
        
    print(f"Greedy: {greedy_val}")
    print(f"Simulated Annealing: {sim_val}")
    display_backpack(greedy_bp, f"Greedy {greedy_val}")
    display_backpack(sim_bp, f"Simulated Annealing {sim_val}")
    display_plot_iter_val(iteration_values)
    

    

main()
