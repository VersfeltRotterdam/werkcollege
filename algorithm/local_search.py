import random
import numpy as np

def _improve(chromosome, distances):
    # used for insertion later
    initial_length = len(chromosome)
    
    for i in range(10):
        # randomly select a node to be inserted into a new position
        random_index = random.randint(0, len(chromosome) - 1)
        node = chromosome[random_index]

        # Let the gene corresponding to random_index be v, then let v be preceeded by u and succeeded by w.
        # Thus, when v is removed from its current position: the connections between (u,v) and (v,w) need to be removed.
        # Hereafter, v will be inserted into a new location. For instance between the genes x and y.
        # hus (x,y) will be removed and (x,v) and (v,y) will be added

        # if the random_index is <= 0, then its predecessor is the origin
        index_u = random_index - 1 if random_index > 0 else  0

        # if the random_index is >= len(chromosome) then its sucessor is the destination
        index_w = random_index + 1 if random_index < (len(chromosome) - 1) else 0

        # the connections between (u,v) and (v,w) are removed, while (u,w) is added
        cost_removal = -distances[index_u, random_index] - distances[random_index, index_w] + distances[index_u, index_w]

        # evaluate the insertion of the random_index after the index
        # where index = -1 corresponds to inserting the random_index right after the starting point
        for index in range(-1, len(chromosome)):
            if index == random_index: continue # do not consider inserting after itself

            index_x = index if index >= 0 else 0
            index_y = index + 1 if index < (len(chromosome) - 1) else 0
            
            # the connections between (x,v) and (v,y) are added, while (x,y) is removed
            new_cost = distances[index_x, random_index] + distances[random_index, index_y] - distances[index_x, index_y]
                      
            # if a cost improvement was detected, apply it and stop looking
            if (cost_removal + new_cost < 0):
                del chromosome[random_index]
                chromosome.insert(index+1, node)
                break
        
    assert len(set(chromosome)) == len(chromosome), f"The chromosome has duplicate genes, which should not be possible."
    assert len(chromosome) == initial_length, f"The size of the chromosome ({len(chromosome)}) is not equal to its initial size ({initial_length}), some genes were lost."
    assert 0 not in chromosome, f"The gene {0} should not be contained in the chromosome, as this is the starting and endpoint"
    # asserts to help you figure out what went wrong
    return chromosome