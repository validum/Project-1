# -*- coding: utf-8 -*-
"""
Created on Tue Sep 02 22:32:49 2014

@author: Eric
"""

import random
import proj1
import matplotlib

#def DPAalg(num_nodes, m):
m = 13
num_nodes = 27770
V = range(m)
E = proj1.make_complete_graph(m)
population = V*len(V)


for new_node in range(m,num_nodes):
    pop_prime = []    
    for idx in range(m):
        pop_prime.append(random.choice(population))
    pop_prime = set(pop_prime)
    population.append(new_node)
    population.extend(pop_prime)
    V.append(new_node)
    E[new_node] = pop_prime

unnormalized_deg_dist = proj1.in_degree_distribution(E)


l1 = unnormalized_deg_dist.keys()

l2=[]
for i in l1:
    temp = unnormalized_deg_dist[i]/27770.0
    l2.append(temp)


matplotlib.pyplot.plot(l1,l2, 'o')
matplotlib.pyplot.title("Log/Log plot of normalized in-degree distribution")
matplotlib.pyplot.ylabel("Probability of in-degree")
matplotlib.pyplot.xlabel("# of in-degree")
matplotlib.pyplot.yscale("log")
matplotlib.pyplot.xscale("log")