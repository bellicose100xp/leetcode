from typing import List
from collections import defaultdict
import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        vertices: int = len(points)

        adj: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

        for i in range(0, vertices - 1):
            for j in range(i + 1, vertices):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d: int = abs(x1-x2) + abs(y1-y2)
                adj[i].append((d, j))
                adj[j].append((d, i))

        seen: set[int] = set([0])
        pq: list[tuple[int, int]] = [*adj[0]]
        heapq.heapify(pq)
        total_cost: int = 0

        while len(seen) < vertices:

            cost, vertex = heapq.heappop(pq)

            if vertex not in seen:
                seen.add(vertex)
                total_cost += cost
                for i in adj[vertex]:
                    heapq.heappush(pq, i)

        return total_cost

solution = Solution()
print(solution.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))