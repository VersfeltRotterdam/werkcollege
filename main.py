from algorithm.genetic_algorithm import GeneticAlgorithm

GA = GeneticAlgorithm(
    population_size=20,
    mutation_bits=4,
    iterations=10_000,
    mutation_active=True,
    local_search_active=False
)
(best_route, score) = GA.solve()
GA.animate_progression()