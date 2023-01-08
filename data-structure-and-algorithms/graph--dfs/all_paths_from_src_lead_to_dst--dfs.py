from typing import Literal, List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.white: Literal[0] = 0
        self.gray: Literal[1] = 1
        self.black: Literal[2] = 2
        self.state: list[Literal[0, 1, 2]] = []

    def hasPathToDst(self, src: int, dst: int, adj: defaultdict[int, list[int]]):
        # if we've reached a gray node then we've found cycle
        if self.state[src] == self.gray:
            return False

        # if we've reached a black_node, return True, as we've already explored this node to reach dst
        if self.state[src] == self.black:
            return True

        # if this is leaf node, then it must be dst for the path to be valid
        if len(adj[src]) == 0:
            return src == dst

        # set the src color to gray and explore outgoing edges
        self.state[src] = self.gray
        for vertex in adj[src]:
            result = self.hasPathToDst(vertex, dst, adj)
            if result == False:
                return False

        self.state[src] = self.black
        return True

    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj: defaultdict[int, list[int]] = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        self.state = [self.white for _ in range(n)]

        return self.hasPathToDst(source, destination, adj)


solution = Solution()
print(solution.leadsToDestination(4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3))  # True
