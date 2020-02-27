# This Python file uses the following encoding: utf-8
import sys
from algorithms import GEP
from setting import _sample_independent_list
from setting import Parameter
import numpy as np
from matplotlib import pyplot as plt
import matplotlib


if __name__ == "__main__":
    plt.figure(figsize=(8, 6), dpi=80)
    g = GEP()
    generation = 1

    while True:
        if generation < Parameter.max_generation:
            plt.figure(figsize=(8, 6), dpi=80)
            g.generate_offspring()
            g.compute_probability()
            print(generation)
            generation = generation + 1
            if generation % 10 == 0:
                plt.clf()
                x = np.arange(0, 90)
                y = np.asarray(_sample_independent_list[10:])
                plt.title('No.' + str(generation) + ' generation')
                plt.xlabel("X")
                plt.xlim(10, 100)

                plt.ylabel("Y")
                plt.ylim(-10, 180)
                plt.plot(x, y, label="actual value")
                plt.plot(x, g.compute_chromosome_value(g.max_fitness_chromosome), label="predictive value")
                plt.text(60, 170, 'Fitness:')
                plt.text(70, 170, str(g.max_fitness))
                plt.text(60, 160, g.show_result())
                plt.legend(loc="upper left", shadow=True)
                plt.pause(0.1)

                pass
            else:
                pass
            if g.max_fitness > Parameter.constraint_constant * Parameter.num_of_samples - 1000:
                break
        pass
    pass







