import numpy as np
import networkx as nx

def compute_flows(g, s):
    inner = 0
    outer = 0
    d_i = dict(zip(list(g.nodes()), np.arange(g.number_of_nodes())))
    n = g.number_of_nodes()
    ad = nx.adjacency_matrix(g)
    s = set(s)
    for e in s:
        if d_i.get(e) is not None:
            for n in nx.neighbors(g, e):
                if n in s:
                    inner += ad[d_i[e], d_i[n]]
                else:
                    outer += ad[d_i[e], d_i[n]]

    return inner, outer


def compute_flows_between(g, s, t):
    flow = 0
    d_i = dict(zip(list(g.nodes()), np.arange(g.number_of_nodes())))
    n = g.number_of_nodes()
    ad = nx.adjacency_matrix(g)
    for e in s:
        for n in t:
            if d_i.get(e) is not None and d_i.get(n) is not None:
                flow += ad[d_i[e], d_i[n]]

    return flow


def weighted_coverage(g, p):
    d_i = dict(zip(np.arange(g.number_of_nodes()), list(g.nodes())))
    n = g.number_of_nodes()
    ad = nx.adjacency_matrix(g)
    p_sum = np.sum(ad) / 2
    num = 0
    for i in range(n):
        for j in range(i + 1, n):
            if p[d_i[i]] == p[d_i[j]]:
                num += ad[i, j]

    return num / p_sum

def find_partitions(p):
    part = dict()
    for k, v in p.items():
        if part.get(v) is None:
            part[v] = [k]
        else:
            part[v].append(k)
    return part
