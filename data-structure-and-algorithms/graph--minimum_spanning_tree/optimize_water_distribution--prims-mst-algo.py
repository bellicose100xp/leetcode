from typing import List
import heapq
from collections import defaultdict


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        adj: dict[int, list[tuple[int, int]]] = defaultdict(list)

        # virtual vertex 0 that represents cost of building well
        # edges are the cost and connects to every house
        for house, cost in enumerate(wells):
            # (cost, house) must be in this order as later we'll create heap from this tuple
            # the heap will use first tuple item's value to insert in correction location in heap
            # if first item has duplicate then second tuple item will be used to make heap insertion decision
            adj[0].append((cost, house + 1))

        # building adj matrix with pipe cost
        for house1, house2, cost in pipes:
            adj[house1].append((cost, house2))
            adj[house2].append((cost, house1))

        # prim's MST algorithm heap
        # heap to retrieve minimum cost to get to next vertex
        # initially we add the virtual edge 0 (but can start with any edge)
        edges = adj[0]
        heapq.heapify(edges)

        # houses visted set
        visited: set[int] = set([0])
        total_cost: int = 0

        # dfs until all edges have been visited
        # "n+1" because we added a virtual node 0
        while len(visited) < n + 1:
            cost, next_house = heapq.heappop(edges)
            if next_house not in visited:
                visited.add(next_house)
                total_cost += cost

                for cost, nei_house in adj[next_house]:
                    if nei_house not in visited:
                        heapq.heappush(edges, (cost, nei_house))

        return total_cost


solution = Solution()
print(solution.minCostToSupplyWater(3, [1, 2, 2],  [[1, 2, 1], [2, 3, 1]]))
