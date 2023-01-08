from typing import List
from collections import defaultdict, deque


class Solution:
    # simplified Hierholzer's Algorithm to find Euler's path
    # - since we have the starting vertex
    # - and the question gurantees that there's a solution (path exits)
    def backtrack(self, vertex: str, flightmap: defaultdict[str, list[str]], result: deque[str]):
        while flightmap[vertex]:
            outgoing_vertex = flightmap[vertex].pop()
            self.backtrack(outgoing_vertex, flightmap, result)

        result.appendleft(vertex)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # adj matrix
        flightmap: defaultdict[str, list[str]] = defaultdict(list)
        for origin, destination in tickets:
            flightmap[origin].append(destination)

        for flights in flightmap.values():
            flights.sort(reverse=True)  # we reversed here so we can pop() lexicographically later

        result: deque[str] = deque()
        self.backtrack("JFK", flightmap, result)
        return list(result)


solution = Solution()
print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
