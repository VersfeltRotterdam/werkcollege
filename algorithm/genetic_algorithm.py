import time
import matplotlib.pyplot as plt

from utils.data_loader import _get_distances
from algorithm.initialisation import _initialize_population
from algorithm.selection import _tournament_selection
from algorithm.crossover import _crossover
from algorithm.mutate import _mutate
from algorithm.local_search import _improve

class GeneticAlgorithm:
    MAX_ITERATIONS = 20_000  # For fairness, do not alter this
    MAX_DURATION = 30  # For fairness, do not alter this
    
    def __init__(self, population_size, mutation_bits, iterations, mutation_active = True, local_search_active = True):
        self.population_size = population_size
        self.distances = _get_distances()
        self.chromosome_size = len(self.distances)-1
        self.mutation_bits = mutation_bits
        self.iterations = iterations
        self.mutation_active = mutation_active
        self.local_search_active = local_search_active
        self.fitness_progression = []
            
    def chromosome_fitness(self, chromosome):
        total_time = 0
        
        # time between the starting node and first pub, cafe or bar
        total_time += self.distances[0][chromosome[0]] 
        
        # time between the consecutive visited pubs, cafes and bars.
        for i in range(1, len(chromosome)):
            total_time += self.distances[chromosome[i-1]][chromosome[i]]
            
        # time between the last pub, cafe or bar and the node where the route started    
        total_time += self.distances[chromosome[len(chromosome)-1]][0]     
          
        return total_time  
    
    def population_fitness(self, population):
        fitness_values = []
        for chromosome in population:
            fitness_values.append(self.chromosome_fitness(chromosome))
        return fitness_values
    
    def solve(self): 
        start_time = time.time()
        # initialize population, evaluate their fitness values and log the best fitness obtained
        population = _initialize_population(self.chromosome_size, self.population_size)
        fitness_values = self.population_fitness(population)

        best_fitness = min(fitness_values)
        best_chromosome = population[fitness_values.index(best_fitness)]

        self.fitness_progression += [best_fitness / 3600] # convert seconds to hours
        
        # main loop of the algorithm
        for _ in range(min(self.MAX_ITERATIONS, self.iterations)):
            if (time.time() - start_time) > self.MAX_DURATION:
                print(f"Exceeded the maximum time of {self.MAX_DURATION} seconds")
                break
            
            # 1. select parents
            parents = _tournament_selection(population, fitness_values)
            
            # 2. create offspring (children)
            child = _crossover(parents)
            
            # 3. mutate and/or educate (improve) the offspring
            if self.mutation_active:
                child = _mutate(child, self.mutation_bits)
            if self.local_search_active: 
                child = _improve(child, self.distances)
            
            # 4. update the population
            if child in population:
                continue

            child_fitness = self.chromosome_fitness(child)
            
            if child_fitness < best_fitness:
                best_fitness = child_fitness
                best_chromosome = child
            
            self.fitness_progression += [best_fitness / 3600] # convert seconds to hours
        
            index, _ = max(enumerate(fitness_values), key=lambda x: x[1])
            if child_fitness < fitness_values[index]:
                population[index] = child
                fitness_values[index] = child_fitness
        
        print(f"Pub crawl solution value of {round(best_fitness / 3600, 2)} hours. Solved the problem in {round(time.time() - start_time, 2)} seconds using {min(self.MAX_ITERATIONS, self.iterations)} iterations.")
        
        return (best_chromosome, best_fitness / 3600) # convert seconds to hours
    
    def animate_progression(self):
        xdata, ydata = list(range(len(self.fitness_progression))), self.fitness_progression
        fig = plt.figure()
        ax1 = fig.add_subplot()             
        ax1.set_ylabel('hours')
        ax1.set_xlabel('iterations')        
        ax1.plot(xdata, ydata)        
        plt.show()
