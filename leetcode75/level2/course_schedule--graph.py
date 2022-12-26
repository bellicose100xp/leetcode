from typing import List
from collections import defaultdict


class Solution:
    """
    v: vertex, e: edge
    Time: O(v+e)
    Space: O(v+e)
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # list of adjacencies (prerequisites) of a vertex
        # defaultdict(list) returns empty list if key doesn't exist in dict
        adjacency_list: dict[int, list[int]] = defaultdict(list)
        cycle_detected: bool = False  # set to True if cycle detected in graph
        # neighbors that were visited in current dfs() call stack
        # graph has a cycle if we come across a neighbor that was previously visited
        visited_set: set[int] = set()
        # neighbors that have already been topologically sorted
        # used here to make the lookup part of alogrithm efficient -- Ex. 'if a in set' --
        # as looking up a value in set is an amortized O(1) time operation
        sorted_set: set[int] = set()
        # list sorted in topological order (prerequisites come before course)
        topologically_sorted_list: list[int] = []

        # make adjacency_lists
        for course, prerequisite in prerequisites:
            adjacency_list[course].append(prerequisite)

        def dfs(vertex: int, visited_set: set[int]):
            nonlocal cycle_detected

            if cycle_detected:
                return

            visited_set.add(vertex)

            for adj in adjacency_list[vertex]:
                # if adj is in sorted set_then move on to next one as we've already explored this path before
                if adj in sorted_set:
                    continue

                # if adj is in visted_set then we've found a cycle in our graph
                if adj in visited_set:
                    cycle_detected = True
                    return

                # recursively explore the adjacency chain
                dfs(adj, visited_set)

            sorted_set.add(vertex)
            topologically_sorted_list.append(vertex)

        for vertex in range(numCourses):
            # clear the visited_set before running dfs() on new vertex
            visited_set = set()

            # this check can also be performed on the topolically_sorted_list but it won't be efficient
            # as list has O(n) time complexity whereas set as O(1)
            if vertex not in sorted_set:
                dfs(vertex, visited_set)

            # if cycle has been detected in graph then no need to continue processing remaining vertices
            # immediately return the empty list [] as it's impossible to finish all courses
            if cycle_detected:
                return []

        return [] if cycle_detected else topologically_sorted_list


solution = Solution()
print(solution.findOrder(2, [[1, 0]]))
print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(solution.findOrder(1, []))
