#!/usr/bin/python

# Project Euler
# Problem 18
# Maximum Path Sum I


import re
import networkx as nx


numerals = re.compile(r'(\d{2})+')
nodes = {}


def make_graph(f_name, max_rows):
    tree = nx.DiGraph()
    with open(f_name, 'r') as triangle:
        line_number = 1
        for line in triangle:
            this_match = numerals.findall(line)
            for column, weight in enumerate(this_match):
                node_id = '{:0>3}'.format(str(line_number)) + '{:0>3}'.format(str(column+1))
                nodes[node_id] = weight
            line_number += 1
    for node, node_value in nodes.items():
        tree.add_node(node, value=node_value)
    for node in nodes:
        line_number = node[0:3]
        column_number = node[3:6]
        if int(line_number) < max_rows:
            neighbor_1 = '{:0>3}'.format(str(int(line_number)+1)) + column_number
            neighbor_2 = '{:0>3}'.format(str(int(line_number)+1)) + '{:0>3}'.format(str(int(column_number)+1))
            edge_1 = tuple([node, neighbor_1, convert_weight(nodes[neighbor_1], 100)])
            edge_2 = tuple([node, neighbor_2, convert_weight(nodes[neighbor_2], 100)])
            neighbors = [edge_1, edge_2]
            tree.add_weighted_edges_from(neighbors)
    return tree


def convert_weight(n, max_value):
    return max_value - int(n)


if __name__ == '__main__':
    source = '001001'
    minimum = ['', '', 1000000]
    total_cost = 0
    D = make_graph(r'c:/temp/Euler/p018_Triangle.txt', 15)
    leaves = [x for x in D.nodes() if D.out_degree(x) == 0]
    leaves.sort()
    for leaf in leaves:
        path = nx.dijkstra_path_length(D, source, leaf)
        if path < minimum[2]:
            minimum = [source, leaf, path]
    shortest_path = nx.dijkstra_path(D, minimum[0], minimum[1])
    for node_ID in shortest_path:
        cost = D.node[node_ID]['value']
        total_cost += int(cost)
        print('Node: {0}, Cost:{1}, Cum Cost:{2}'.format(node_ID, cost, total_cost))
