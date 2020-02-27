import copy
import math
import random as rd
import chromosome
from setting import Parameter
import genetic_operator as go
from concurrent.futures import ThreadPoolExecutor, as_completed
from expression_tree import ExpressionTree as e_t


class GEP(object):
    def __init__(self):
        self.probability = list()
        self.max_fitness = 0
        self.max_fitness_chromosome = None
        self.population = list()
        self.max_fitness_index = None
        self.sum_of_fitness = 0
        self.repeat_times = 0

        while True:
            self.population.clear()
            for i in range(Parameter.population_size):
                c = chromosome.Chromosome()
                c.fitness = self.compute_chromosome_fitness(self.compute_chromosome_value(c), i)
                self.population.append(c)
            self.compute_max_fitness()

            if self.max_fitness != 0:
                break
        # print('Num of generation: 1')
        self.compute_probability()
        # self.display()

    def compute_max_fitness(self):
        flag = False
        self.max_fitness_index = Parameter.population_size
        for i in range(Parameter.population_size - 1):
            if self.max_fitness < self.population[i].fitness:
                flag = True
                self.max_fitness = self.population[i].fitness
                self.max_fitness_index = i + 1
                self.max_fitness_chromosome = copy.deepcopy(self.population[i])
        if flag:
            self.repeat_times = 0
        else:
            self.repeat_times = self.repeat_times + 1

    def show_result(self) -> list:
        # print('Result: Max No.' + str(self.max_fitness_index))
        result = list()
        for i in range(Parameter.num_of_genes):
            et = e_t(self.population[self.max_fitness_index - 1].genes[i].genotype)
            et.create()
            result.append(et.infix_expression)
        # print(result)
        result_str = ''
        for i in range(Parameter.num_of_genes):
            result_str = result_str + ''.join(result[i])
            result_str = result_str + ' + '
        # print(result_str[0: -3])
        return result_str[0: -3]

    def run(self) -> None:
        generation = 1
        while True:
            generation = generation + 1
            if generation < Parameter.max_generation:
                self.generate_offspring()
                self.compute_probability()
                if generation % 10 == 0:
                    print('=====================================================')
                    self.display()
                    print('Max fitness value: ' + str(self.max_fitness))
                    print('Num of generation: ' + str(generation))
                    print('=====================================================')
            else:
                self.show_result()
                break
            if self.max_fitness > Parameter.constraint_constant * Parameter.num_of_samples - 1000:
                self.show_result()
                break
        pass

    def display(self):
        for i in range(Parameter.population_size):
            print('No.' + str(i + 1) + ' Fitness: ' + str(self.population[i].fitness))
            print(self.population[i].genotype)

    def generate_offspring(self) -> None:
        offspring_list = list()
        obj_list = list()
        self.sum_of_fitness = 0

        executor = ThreadPoolExecutor(max_workers=Parameter.population_size - 1)
        for i in range(Parameter.population_size - 1):
            selected_chromosome = copy.deepcopy(self.population[self.roulette_wheel_selection()])
            obj = executor.submit(self.evolution, selected_chromosome, i)
            obj_list.append(obj)

        for future in as_completed(obj_list):
            offspring_list.append(future.result())
            pass
        self.population = offspring_list
        self.compute_max_fitness()
        self.population.append(self.max_fitness_chromosome)

    def compute_probability(self):
        self.probability.clear()
        for i in range(Parameter.population_size):
            self.probability.append(self.population[i].fitness / self.sum_of_fitness)

    def evolution(self, selected_chromosome: chromosome.Chromosome, chromosome_index: int):
        # mutation
        if self.operation_selection(Parameter.mutation_rate + self.repeat_times / Parameter.max_generation):
            go.mutation(selected_chromosome)

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
            next_chromosome = copy.deepcopy(self.population[self.roulette_wheel_selection()])
            selected_chromosome = go.one_point_recombination(selected_chromosome, next_chromosome)

        # two point recombination
        if self.operation_selection(Parameter.two_point_recombination_rate):
            next_chromosome = copy.deepcopy(self.population[self.roulette_wheel_selection()])
            selected_chromosome = go.two_point_recombination(selected_chromosome, next_chromosome)

        # gene recombination
        if self.operation_selection(Parameter.gene_recombination_rate):
            next_chromosome = copy.deepcopy(self.population[self.roulette_wheel_selection()])
            selected_chromosome = go.gene_recombination(selected_chromosome, next_chromosome)

        selected_chromosome.fitness = \
            self.compute_chromosome_fitness(self.compute_chromosome_value(selected_chromosome), chromosome_index)

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

    def compute_chromosome_fitness(self, chromosome_value_list: list, chromosome_index: int) -> float:
        fitness = fitness_func(chromosome_value_list)
        if fitness < 0:
            return 0
        else:
            self.sum_of_fitness = self.sum_of_fitness + fitness
            return fitness

    def compute_chromosome_value(self, c: chromosome.Chromosome) -> list:
        chromosome_value_list = list()
        for sample_index in range(Parameter.num_of_samples):
            chromosome_value = 0
            for gene_index in range(Parameter.num_of_genes):
                chromosome_value = \
                    chromosome_value + \
                    gene_read_compute_machine(sample_index, list(c.genes[gene_index].genotype))
            chromosome_value_list.append(chromosome_value)
        return chromosome_value_list


def fitness_func(current_values: list, func_type: str = 'Absolute') -> float:
    fitness_var = 0
    true_values = Parameter.sample_dependent_variable
    M = Parameter.constraint_constant
    if func_type == 'Absolute':
        for i in range(Parameter.num_of_samples):
            fitness_var = fitness_var + (M - abs(current_values[i] - true_values[i]))
    return fitness_var


def pre_gene_read_compute_machine(genotype: list, sample_independent) -> float:
    """

    :param genotype:
    :param sample_independent:
    :return:
    """
    valid_length = get_gene_valid_length(genotype)
    index = valid_length
    try:
        while True:
            if genotype[index] in sample_independent:
                genotype[index] = sample_independent.get(genotype[index])
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

