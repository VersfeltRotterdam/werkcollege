import random
import numpy as np

def _crossover(parents):   
    parent1 = parents[0]
    parent2 = parents[1]

    # use a random mask to select genes from the first parent
    mask = np.zeros(len(parent1), dtype=int)
    mask[:int(len(parent1)/2)] = 1
    np.random.shuffle(mask)
    mask = mask.astype(bool)
    
    child = np.array(parent1)[mask].tolist()
    
    for node in parent2:
        if node not in child:
            child += [node]
    
    # asserts to help you figure out what went wrong        
    assert len(set(child)) == len(child), f"The child chromosome has duplicate genes, which should not be possible."
    assert len(child) == len(parent1), f"The size of the child chromosome ({len(child)}) is not equal to the size of the parents ({len(parent1)}), some genes were lost."
    assert 0 not in child, f"The gene {0} should not be contained in the chromosome, as this is the starting and endpoint"
    
    return child