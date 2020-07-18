import networkx as nx
import numpy as np
from ged4py.algorithm import graph_edit_dist
from numpy import genfromtxt

def graphsimilarity_scores(A1,A2):
    G1 = nx.from_numpy_matrix(A1,create_using = nx.DiGraph)
    G2 = nx.from_numpy_matrix(A2,create_using = nx.DiGraph)
    k  = graph_edit_dist.compare(G1,G2,print_details = False)
    return k
