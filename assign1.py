# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 17:48:36 2014

@author: Cire
"""

"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
import proj1
import matplotlib


# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

citation_graph = load_graph(CITATION_URL)

unnormalized_deg_dist = proj1.in_degree_distribution(citation_graph)

l1 = sorted(unnormalized_deg_dist.keys())

l2=[]
for i in l1:
    temp = unnormalized_deg_dist[i]/27770.0
    l2.append(temp)

matplotlib.pyplot.loglog(l1,l2)
matplotlib.pyplot.title("Log/Log plot of normalized in-degree distribution")
matplotlib.pyplot.ylabel("Probability of in-degree")
matplotlib.pyplot.xlabel("# of in-degree")

#file = open("whereami.txt", "w")
#
#for key in unnormalized_deg_dist.keys():
#    file.write(repr(key) + "\n")
#file.close()

