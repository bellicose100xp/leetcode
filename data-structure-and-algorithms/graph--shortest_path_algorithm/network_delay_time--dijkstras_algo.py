from typing import List
import heapq
from sys import maxsize
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        for i, j, w in times:
            adj[i].append((w, j))

        seen: set[int] = set()
        # weight for 'n' will be at 'n-1' since list is 0-idx based
        weights: list[int] = [maxsize]*n
        # initialize weight of 'k' node to '0' as this is the src node
        weights[k-1] = 0
        pq: list[tuple[int, int]] = [(0, k)]
        heapq.heapify(pq)

        while pq:
            curr_weight, curr_node = heapq.heappop(pq)

            if curr_node in seen:
                continue

            seen.add(curr_node)

            for nei_weight, nei_node in adj[curr_node]:
                if nei_node not in seen:
                    # accumulated shortest path weight to get this neibhbor
                    acc_weight: int = curr_weight + nei_weight

                    # if acc_weight is less than the already found shortest weight
                    # then we replace the weights[nei] with the new shortest weight
                    if acc_weight < weights[nei_node - 1]:
                        weights[nei_node - 1] = acc_weight
                        heapq.heappush(pq, (acc_weight, nei_node))

        return max(weights) if len(seen) == n else -1
