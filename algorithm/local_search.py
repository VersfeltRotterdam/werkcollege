import random
import numpy as np

def _improve(chromosome, distances):
    # used for insertion later
    initial_length = len(chromosome)
            
    assert len(set(chromosome)) == len(chromosome), f"The chromosome has duplicate genes, which should not be possible."
    assert len(chromosome) == initial_length, f"The size of the chromosome ({len(chromosome)}) is not equal to its initial size ({initial_length}), some genes were lost."
    assert 0 not in chromosome, f"The gene {0} should not be contained in the chromosome, as this is the starting and endpoint"
    # asserts to help you figure out what went wrong
    return chromosome