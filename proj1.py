# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 11:32:05 2014

@author: Cire
"""

EX_GRAPH0 = {0:set([1,2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}


#print EX_GRAPH0
#print EX_GRAPH1
#print EX_GRAPH2


def make_complete_graph(num_nodes):
    complete_digraph = {}
    for node in range(num_nodes):
        lst = range(num_nodes)
        lst.remove(node)
        complete_digraph[node] = set(lst)
    return complete_digraph
        
    
def compute_in_degrees(digraph):
    indegree_dict = digraph.copy()
    print indegree_dict
    for key in indegree_dict.keys():
        indegree_dict[key] = 0
    for key in digraph.keys():
        hnode = digraph[key]
        for idx in hnode:
            indegree_dict[idx] = indegree_dict[idx]+1
    return indegree_dict



#kkk = compute_in_degrees(EX_GRAPH1)
#
#print kkk

#j=10
#print j
#
#list = range(j)
#list.remove(5)
#print list
#
#dict = {}
#dict[3] = set(list)
#print dict
#
#bbb = make_complete_graph(5)
#
#print bbb

#testdict = EX_GRAPH1.copy() 
#
#
#print testdict
#
#for key in testdict.keys():
#    testdict[key] = 0
#    testdict[key] = testdict[key]+1
#    
#print testdict
#print EX_GRAPH1
#for key in EX_GRAPH1.keys():
#    j = EX_GRAPH1[key]
#    for ind in j:
#        print ind
