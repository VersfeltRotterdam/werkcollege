import random
import numpy as np

def _mutate(chromosome, mutation_bits):
    # randomly swap visited nodes {mutation_bits} times
    for i in range(mutation_bits):
        # select two random indices to swap
        first_index, second_index = random.sample(range(0, len(chromosome)), 2)
                
        temp = chromosome[first_index]
        chromosome[first_index] = chromosome[second_index]
        chromosome[second_index] = temp
    
    # asserts to help you figure out what went wrong
    assert len(set(chromosome)) == len(chromosome), f"The child chromosome has duplicate genes, which should not be possible."
    assert 0 not in chromosome, f"The gene {0} should not be contained in the chromosome, as this is the starting and endpoint"
    
    return chromosome