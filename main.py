import warnings
warnings.filterwarnings('ignore')
import osmnx as ox
import pandas as pd

from algorithm.genetic_algorithm import GeneticAlgorithm
from utils.plot import _plot_route
from utils.sent_score import _sent_score

GA = GeneticAlgorithm(
    population_size=60,
    mutation_bits=4,
    iterations=10_000,
    mutation_active=True,
    local_search_active=True
)
(best_route, score) = GA.solve()
GA.animate_progression()