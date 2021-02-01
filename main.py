import matplotlib
import numpy as np
import random

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

class person():
    def newOpinion(self):
        opinion = random.uniform(0,1)
        certainty = random.uniform(0,1)
        return (opinion, certainty)

ly = []
for j in range(10000):
    plt.clf()
    x = []
    y = []
    population = []
    for i in range(1, 100, 1):
        population.append(person())
        opinions = []
        certainties = []
        for p in population:
            c = p.newOpinion()
            opinions.append(c[0])
            certainties.append(c[1])
        x.append(i)
        y.append(np.average(opinions, weights=certainties))
    ly.append(y)
    rang = np.linspace(0,100,20)

    for o in rang:
        plt.plot(x, np.percentile(ly, o, axis=0))
    plt.draw()
    plt.pause(0.00001)