from typing import List
from sys import maxsize
from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        min_routes: int = maxsize
        visited_bus_stops: set[int] = set()
        adjacencies: dict[int, set[int]] = defaultdict(set)

        for route in routes:
            for curr_stop in route:
                adjacencies[curr_stop].update([stop for stop in route if stop != curr_stop])

        def travel(bus_stop: int):
            nonlocal min_routes

            # visited_set keeps tracks of buses taken so far
            visited_bus_stops.add(bus_stop)

            if target in adjacencies[bus_stop]:
                buses_taken: int = len(visited_bus_stops)
                min_routes = min(min_routes, buses_taken)
            else:
                for stop in adjacencies[bus_stop]:
                    if stop not in visited_bus_stops:
                        travel(stop)

            visited_bus_stops.remove(bus_stop)

        travel(source)

        return -1 if min_routes == maxsize else min_routes


solution = Solution()
print(solution.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
print(solution.numBusesToDestination([[1, 2, 7], [3, 6, 5], [8, 1, 4], [6, 12, 10], [9, 7, 5]], 1, 6))

# time limit exceeded
# print(solution.numBusesToDestination([[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]], 7, 47))
