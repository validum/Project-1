# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 11:32:05 2014

@author: Cire
"""
import matplotlib
EX_GRAPH0 = {0:set([1,2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    "creates dictionary with all possible edges, no self loop"
    complete_digraph = {}
    for node in range(num_nodes):
        lst = range(num_nodes)
        lst.remove(node)
        complete_digraph[node] = set(lst)
    return complete_digraph
        
    
def compute_in_degrees(digraph):
    "computes ind-degrees for a digraph represented as a dictionary"
    indegree_dict = digraph.copy()
    for key in indegree_dict.keys():
        indegree_dict[key] = 0
    for key in digraph.keys():
        hnode = digraph[key]
        for idx in hnode:
            indegree_dict[idx] = indegree_dict[idx]+1
    return indegree_dict


def in_degree_distribution(digraph):
    "takes digraph represented as dictionary and returns unnormalized in-degree distribution"
    degree_dist = {}
    digraph_in_degrees = compute_in_degrees(digraph)
    for key in digraph_in_degrees.keys():
        num_nodes = digraph_in_degrees[key]
        if num_nodes in degree_dist:
            degree_dist[num_nodes] = degree_dist[num_nodes] + 1
        else:
            degree_dist[num_nodes] = 1
    return degree_dist

