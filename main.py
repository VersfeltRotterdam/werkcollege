from utils.sent_score import _sent_score
from algorithm.genetic_algorithm import GeneticAlgorithm

GA = GeneticAlgorithm(
    population_size=20,
    mutation_bits=4,
    iterations=10_000,
    mutation_active=True,
    local_search_active=True
)
(best_route, score) = GA.solve()
GA.animate_progression()

# Uncomment the code below if you want to sent in your scores for the competition

# team_name = ""
# _sent_score(team_name, score, best_route)