import itertools
from time import perf_counter
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import json
import sys
def generate_visualisation(graph):
    nx.draw(graph, with_labels = True)
    plt.savefig("graph_image.png")

def isVertexesCreateClique(array, vertexes):
    size = len(vertexes)
    for i in range(0, len(vertexes)):
        isCliques = True
        for j in vertexes:
            for k in vertexes:
                if j == k : continue
                if array[j][k] != 1: isCliques = False
        if(isCliques==True) : 
            return vertexes

def max_cliques(A, vertexes):
    is_clique_found_flag = False
    cliques = []
    cliques_with_different_vertexes = []
    start = perf_counter()
    for i in range(len(vertexes)+1, 1, -1):
            for l in itertools.combinations(vertexes, i):
                result = isVertexesCreateClique(A, l)
                if result != None:
                    the_biggest_clique = len(l) 
                    cliques.append(l)
                    is_clique_found_flag = True
            if(is_clique_found_flag) : break
    
    max_cliques = []
    for element in cliques:
        if len(element) == the_biggest_clique: 
            max_cliques.append(element)

    for c in range (0, len(max_cliques)):
        unique_flag = True
        if c == 0: 
            cliques_with_different_vertexes.append(max_cliques[c])
            continue
        for element in cliques_with_different_vertexes:
            for vertex in max_cliques[c]:
                if vertex in element: unique_flag = False
        if(unique_flag): cliques_with_different_vertexes.append(max_cliques[c])

    stop = perf_counter()
    print("Total time:: ", stop - start)
    print("Maximum cliques in graph: ", end = "")
    for el in cliques_with_different_vertexes:
        print(el, end= " ")
        
def find_clique_in_random_generated_graph(number_of_vertexes, posiibility):
    vertexes = []
    number_of_vertex = number_of_vertexes
    possibility_of_creating_edge = posiibility
    G = nx.erdos_renyi_graph(number_of_vertex, possibility_of_creating_edge, seed = None, directed = False)
    adjency_matrix = nx.to_numpy_matrix(G)
    print("Adjency array for graph:\n", adjency_matrix)
    A = np.ndarray.tolist(adjency_matrix)
    for i in range(0, number_of_vertex):
        for j in range(0, number_of_vertex):
            A[i][j] = int(A[i][j])
    generate_visualisation(G)  
    for i in range(number_of_vertex):
        vertexes.append(i)
    max_cliques(A, vertexes)

def load_json_data():
    json_file = open('edges.json')
    data_json = json.load(json_file)
    graph = nx.Graph()
    vertexes = []
    for i in data_json['edges']:
        print(i['from'])  
        graph.add_edge(i['from'], i['to'])
        vertexes.append(i['from'])
        vertexes.append(i['to'])
    vertexes = list(set(vertexes))
    adjency_matrix = nx.to_numpy_matrix(graph)

    A = np.ndarray.tolist(adjency_matrix)
    max_cliques(A, vertexes)

def batch_processing():
    if __name__ == "__main__":
        graph = nx.Graph()
        vertexes = []
        for line in sys.stdin:
            if(len(line.strip()) > 3):
                print("Wrong data format!")
                exit()
            graph.add_edge(int(line[0]), int(line[2]))
            vertexes.append(int(line[0]))
            vertexes.append(int(line[2]))

        vertexes = list(set(vertexes))
        adjency_matrix = nx.to_numpy_matrix(graph)

        A = np.ndarray.tolist(adjency_matrix)
        max_cliques(A, vertexes)

find_clique_in_random_generated_graph(3, 0.5)

