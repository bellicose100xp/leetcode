from __future__ import annotations
from typing import List, Optional  # type: ignore
from collections import deque

# Definition for a binary tree node.


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None):
        self.val: int = val
        self.neighbors: list[Node] | None = neighbors


class Graph:
    def buildGraphLeetCode(self, arr: list[list[int]]) -> Node | None:
        head: Node = Node(0)

        node_tracker: dict[int, Node] = {0: head}
        neighbors_array: list[list[Node]] = []

        # convert all neighbors to Node() in new neighbors_array matrix
        for neighbors in arr:
            neighbor_nodes_list: list[Node] = []
            for nei in neighbors:
                if nei not in node_tracker:
                    node_tracker[nei] = Node(nei)
                neighbor_nodes_list.append(node_tracker[nei])
            neighbors_array.append(neighbor_nodes_list)

        # add neighbors list to each corresponding node
        for node_val, neighbors_list in enumerate(neighbors_array):
            node_tracker[node_val].neighbors = neighbors_list

        return head

# utility functions


def printUndirectedGraph(root: Node | None) -> None:
    graph: dict[int, list[int]] = {}
    queue: deque[Node | None] = deque([root])
    seen: set[Node] = set()

    while queue:
        node = queue.pop()
        if node and node not in seen:
            seen.add(node)
            if node.neighbors:
                nei_val_list: list[int] = []
                for nei in node.neighbors:
                    if nei not in seen:
                        queue.appendleft(nei)
                    nei_val_list.append(nei.val)
                graph[node.val] = nei_val_list

    sorted_graph_keys: list[int] = list(sorted(graph))
    print(sorted_graph_keys)
    adj_matrix: list[list[int]] = [[] for _ in range(sorted_graph_keys[-1]+1)]

    for idx in sorted_graph_keys:
        adj_matrix[idx] = graph[idx]

    print(adj_matrix)


tree = Graph()
leet = [[1, 3], [0, 2], [1, 3], [0, 2]]
root = tree.buildGraphLeetCode(leet)
printUndirectedGraph(root)
