#!/bin/python

graph = {}

def initialize(graph):
    with open("input9.txt") as f:
        for line in f:
            line = line[:-1].split(' ')
            if line[0] not in graph.keys():
                graph[line[0]] = {}
            graph[line[0]][line[2]] = int(line[4])
            if line[2] not in graph.keys():
                graph[line[2]] = {}
            graph[line[2]][line[0]] = int(line[4])


def dijkstra(graph, src, dest):
    if src not in graph:
        raise TypeError('src is not in the graph')
    if dest not in graph:
        raise TypeError('dest is not in the graph')
    if src == None or dest == None:
        raise TypeError('src or dest is None')
    print(src, dest)
    visited = []
    tab = {}
    for loc in graph.keys():
        if loc == src:
            tab[src] = 0
        else:
            tab[loc] = -1
    loc = src
    while dest not in visited:
        visited.append(loc)
        next_loc = None
        print(loc, visited)
        try:
            for child in graph[loc].keys():
                print("-", child)
                if (child not in visited) and (tab[child] > tab[loc] + graph[loc][child] or tab[child] == -1):
                    tab[child] = tab[loc] + graph[loc][child]
                    if next_loc == None or tab[child] < tab[next_loc]:
                        next_loc = child
            loc = next_loc
        except Exception as e:
            print(tab)
            raise e
    print("RESULTAT :", src, dest, tab[dest])
    return tab[dest]

def find_shortest(graph):
    res = None
    for a in graph.keys():
        dist = 0
        last_location = a
        for b in graph.keys():
            if a != b:
                tmp = dijkstra(graph, a, b)
                if res is None or tmp < res:
                    res = tmp
    return res

if __name__ == "__main__":
    initialize(graph)
    # print(graph)
    find_shortest(graph)
