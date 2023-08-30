import random
import numpy as np

def _initialize_population(chromosome_size, population_size):
    population = []
    
    # randomly initialize the population
    for i in range(population_size):
        chromosome = list(range(1, chromosome_size+1))
        random.shuffle(chromosome)
        population.append(chromosome)
    
    # asserts to help you figure out what went wrong
    assert len(population) == population_size, f"The generated population size ({len(population)}) does not equal the user specified size ({population_size})."
    for chromosome in population:
        assert len(set(chromosome)) == len(chromosome), f"The generated chromosome has duplicated genes."
        assert len(chromosome) == chromosome_size, f"The generated chromosome size ({len(chromosome)}) does not equal the correct size ({chromosome_size})."
        assert 0 not in chromosome, f"The gene {0} should not be contained in the chromosome, as this is the starting and endpoint"

    return population