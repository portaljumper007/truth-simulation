import matplotlib
import numpy as np
import random

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D


class person():
    def newOpinion(self):
        opinion = 1 - (random.uniform(0,1) ** 20)
        certainty = random.uniform(0,1)
        return (opinion, certainty)

ly = []
lx = []
for j in range(1,100000000):
    x = []
    y = []
    population = []
    rang = np.linspace(0,1000,100)
    for i in rang:
        population.append(person())
        opinions = []
        certainties = []
        for p in population:
            c = p.newOpinion()
            opinions.append(c[0])
            certainties.append(c[1])
        x.append(i)
        y.append(np.average(opinions, weights=certainties))
    #lx.extend(x)
    #ly.extend(y)
    ly.append(y)
    #lz = ly - np.average(ly, axis=0)
    rang = np.linspace(0,100,15)
    if j % 5 == 0:
        plt.clf()
    #plt.tricontour(lx, ly, lz, 15, linewidths=0.5, colors='k')
        for o in rang:
            plt.plot(x, np.percentile(ly, o, axis=0))
    plt.draw()
    plt.pause(0.0000001)