import random
import numpy as np

def _tournament_selection(population, fitness_values):
    
    # randomly select 4 chromosomes from the population
    indices = random.sample(range(0, len(population)), 4)

    # create 2 binary tournaments and return its 2 winners
    parents = []
    for i in range(2):
        if fitness_values[indices[i*2]] < fitness_values[indices[i*2+1]]:
            parents.append(population[indices[i*2]])
        else:
            parents.append(population[indices[i*2+1]])
            
    # asserts to help you figure out what went wrong
    assert len(parents) == 2, f"Expected two parents, got {len(parents)}"        

    return parents