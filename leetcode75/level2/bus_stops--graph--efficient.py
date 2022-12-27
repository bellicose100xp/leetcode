from typing import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # base case
        if source == target:
            return 0

        # converting all bus_stop lists in routes to set()
        # this would help with efficient lookup O(1) (ex. item in set) later
        routes_set: list[set[int]] = list(map(set, routes))

        # create a dictionary of bus vertices that can reached by another bus
        # use set() as it would help with O(1) lookup operation later
        bus_neighbors: dict[int, set[int]] = defaultdict(set)

        # create a dict of bus neighbors that have at least one common stop
        for bus, bus_stops in enumerate(routes_set):
            for next_bus in range(bus + 1, len(routes_set)):
                next_bus_stops = routes_set[next_bus]
                # if any bus stops match in either bus's route, add both buses as each others neighbors
                if any([bus_stop in next_bus_stops for bus_stop in bus_stops]):
                    bus_neighbors[bus].add(next_bus)
                    bus_neighbors[next_bus].add(bus)

        # visited: set of all buses that we've taken
        # fill visited set with our starting point (all bus whose routes that contain source)
        visited: set[int] = set()

        # target: set of all buses that can reach our target bus stop
        targets: set[int] = set()

        for bus, bus_stops in enumerate(routes_set):
            if source in bus_stops:
                visited.add(bus)
            if target in bus_stops:
                targets.add(bus)

        # next_bus_queue = [(next_bus_to_take, number_of_trips_it_takes_to_get_to_any_bus_stop_of_the_next_bus)]
        # initialize it with all the buses that contain the source bus stop
        # you only need to take 1 trip to get to any of the source bus's stops
        next_bus_queue: deque[tuple[int, int]] = deque([(bus, 1) for bus in visited])

        # iterate over the next_bus_queue until the target bus stop is found or the queue is exhausted
        while next_bus_queue:
            next_bus, trips = next_bus_queue.popleft()
            # target is preset in next_bus's routes return the number of trips it took to get there
            if target in routes_set[next_bus]:
                return trips

            # explore routes of other bus's that are directly connected to this bus's routes
            for neighbor in bus_neighbors[next_bus]:
                # if we have already visited this neighboring bus then we don't need to take it again
                if neighbor not in visited:
                    # otherwise add the neighboring bus to the next_bus_queue to be explored later
                    # add +1 to the trips since it would take 1 additional trip to reach any of neighboring bus's stops
                    next_bus_queue.append((neighbor, trips + 1))
                    # add this neighboring bus to all the buses we've already taken so we don't take them again
                    visited.add(neighbor)

        # if we have not reached the target by any route from source then return -1
        return -1


solution = Solution()
print(solution.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
print(solution.numBusesToDestination([[1, 2, 7], [3, 6, 5], [8, 1, 4], [6, 12, 10], [9, 7, 5]], 1, 6))
print(solution.numBusesToDestination([[25, 33], [3, 5, 13, 22, 23, 29, 37, 45, 49], [15, 16, 41, 47], [5, 11, 17, 23, 33], [10, 11, 12, 29, 30, 39, 45], [2, 5, 23, 24, 33], [1, 2, 9, 19, 20, 21, 23, 32, 34, 44], [7, 18, 23, 24], [1, 2, 7, 27, 36, 44], [7, 14, 33]], 7, 47))
