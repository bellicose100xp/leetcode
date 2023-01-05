from typing import List
from collections import defaultdict


class Solution:

    def dfs(self, i: int, adj: dict[int, list[int]], visited: set[int], component_nodes: list[int]) -> None:
        visited.add(i)
        component_nodes.append(i)
        for nei in adj[i]:
            if nei not in visited:
                self.dfs(nei, adj, visited, component_nodes)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        _s: list[str] = list(s)
        adj: dict[int, list[int]] = defaultdict(list)

        for x, y in pairs:
            adj[x].append(y)
            adj[y].append(x)

        visited: set[int] = set()

        for i in adj:
            component_nodes: list[int] = []
            if i not in visited:
                self.dfs(i, adj, visited, component_nodes)

                component_str: list[str] = [_s[i] for i in component_nodes]
                component_str.sort()
                component_nodes.sort()

                for char, idx in zip(component_str, component_nodes):
                    _s[idx] = char  # place sorted chars back in component indices\

        return "".join(_s)


solution = Solution()
print(solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]))  # ? bacd
print(solution.smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]])) #? abcd
print(solution.smallestStringWithSwaps("cba", [[0,1],[1,2]])) #? abc
