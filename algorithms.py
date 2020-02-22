import copy
import math
import random as rd
import chromosome
from setting import Parameter
import genetic_operator as go
from concurrent.futures import ThreadPoolExecutor, as_completed


class GEP(object):
    def __init__(self):
        self.probability = list()
        self.max_fitness = 0
        self.population = list()
        self.max_fitness_index = None
        sum_of_fitness = 0

        while True:
            self.population.clear()
            for i in range(Parameter.population_size):
                c = chromosome.Chromosome()
                c.fitness = compute_chromosome_fitness(compute_chromosome_value(c))
                self.population.append(c)
                sum_of_fitness = sum_of_fitness + c.fitness
                if self.max_fitness < c.fitness:
                    self.max_fitness = c.fitness
                    self.max_fitness_index = i
            if self.max_fitness != 0:
                break

        for i in range(Parameter.population_size):
            self.probability.append(self.population[i].fitness / sum_of_fitness)

    def run(self) -> None:
        generation = 1
        while True:
            self.population = self.generate_offspring()
            generation = generation + 1
        pass

    def generate_offspring(self) -> list:
        offspring_list = list()
        sum_of_fitness = 0

        executor = ThreadPoolExecutor(max_workers=Parameter.population_size)
        for i in range(Parameter.population_size):
            selected_chromosome = self.population[self.roulette_wheel_selection()]
            offspring = executor.submit(self.evolution, selected_chromosome)
            offspring_list.append(offspring)

        for future in as_completed(offspring_list):
            pass
        return offspring_list

    def evolution(self, selected_chromosome: chromosome.Chromosome):
        # mutation
        if self.operation_selection(Parameter.mutation_rate):
            go.gene_transposition(selected_chromosome)

        # IS transposition
        if self.operation_selection(Parameter.IS_transposition_rate):
            go.insert_transposition(selected_chromosome)

        # RIS transposition
        if self.operation_selection(Parameter.RIS_transposition_rate):
            go.root_insert_transposition(selected_chromosome)

        # gene transposition
        if self.operation_selection(Parameter.gene_transposition_rate):
            go.root_insert_transposition(selected_chromosome)

        # one point recombination
        if self.operation_selection(Parameter.one_point_recombination_rate):
            next_chromosome = self.population[self.roulette_wheel_selection()]
            selected_chromosome = go.one_point_recombination(selected_chromosome, next_chromosome)

        # two point recombination
        if self.operation_selection(Parameter.two_point_recombination_rate):
            next_chromosome = self.population[self.roulette_wheel_selection()]
            selected_chromosome = go.two_point_recombination(selected_chromosome, next_chromosome)

        # gene recombination
        if self.operation_selection(Parameter.gene_recombination_rate):
            next_chromosome = self.population[self.roulette_wheel_selection()]
            selected_chromosome = go.gene_recombination(selected_chromosome, next_chromosome)

        return selected_chromosome

    def roulette_wheel_selection(self) -> int:
        rand = rd.random()
        probability_total = 0
        select_index = 0
        for i in range(Parameter.population_size):
            probability_total = probability_total + self.probability[i]
            if probability_total >= rand:
                select_index = i
                break
        return select_index

    @staticmethod
    def operation_selection(probability):
        rand = rd.random()
        if rand <= probability:
            return True
        else:
            return False


def fitness_func(current_values: list, func_type: str = 'Absolute') -> float:
    fitness_var = 0
    true_values = Parameter.sample_dependent_variable
    M = Parameter.constraint_constant
    if func_type == 'Absolute':
        for i in range(Parameter.num_of_samples):
            fitness_var = fitness_var + (M - abs(current_values[i] - true_values[i]))
    return fitness_var


def gene_read_compute_machine(sample_index: int, genotype: list) -> float:
    """

    :param sample_index:
    :param genotype:
    :return:
    """
    valid_length = get_gene_valid_length(genotype)
    index = valid_length
    try:
        while True:
            if genotype[index] in Parameter.sample_independent_list[sample_index]:
                genotype[index] = Parameter.sample_independent_list[sample_index].get(genotype[index])
            else:
                if genotype[index] == '+':
                    genotype[index] = genotype[valid_length - 1] + genotype[valid_length]
                    valid_length = valid_length - 2
                elif genotype[index] == '-':
                    genotype[index] = genotype[valid_length - 1] - genotype[valid_length]
                    valid_length = valid_length - 2
                elif genotype[index] == '*':
                    genotype[index] = genotype[valid_length - 1] * genotype[valid_length]
                    valid_length = valid_length - 2
                elif genotype[index] == '/':
                    genotype[index] = genotype[valid_length - 1] / genotype[valid_length]
                    valid_length = valid_length - 2
                elif genotype[index] == 'Q':
                    genotype[index] = genotype[valid_length] ** (1 / 2)
                    valid_length = valid_length - 1
                elif genotype[index] == 'L':
                    genotype[index] = math.log2(genotype[valid_length])
                    valid_length = valid_length - 1
                elif genotype[index] == 'S':
                    genotype[index] = math.sin(genotype[valid_length])
                    valid_length = valid_length - 1
                elif genotype[index] == 'C':
                    genotype[index] = math.cos(genotype[valid_length])
                    valid_length = valid_length - 1
            index = index - 1
            if index < 0:
                break
    except (ZeroDivisionError, ValueError) as e:
        return 0
    return genotype[0]


def get_gene_valid_length(genotype: list) -> int:
    former = 0
    latter = 0
    while True:
        if genotype[former] in Parameter.operand:
            latter = latter + Parameter.operand.get(genotype[former])
        if former == latter:
            break
        former = former + 1
    return former


def compute_chromosome_fitness(chromosome_value_list: list) -> float:
    return fitness_func(chromosome_value_list)


def compute_chromosome_value(c: chromosome.Chromosome) -> list:
    chromosome_value_list = list()
    for sample_index in range(Parameter.num_of_samples):
        chromosome_value = 0
        for gene_index in range(Parameter.num_of_genes):
            chromosome_value = \
                chromosome_value + \
                gene_read_compute_machine(sample_index, c.genes[gene_index])
        chromosome_value_list.append(chromosome_value)
    return chromosome_value_list
