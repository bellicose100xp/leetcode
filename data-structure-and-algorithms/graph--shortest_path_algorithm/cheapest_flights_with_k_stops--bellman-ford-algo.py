from typing import List
from sys import maxsize


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        prev_cost: list[int] = [maxsize]*n
        prev_cost[src] = 0  # since we start at source, initail cost fo src is 0
        next_cost: list[int] = [maxsize]*n

        # number of times to iterate
        while k >= 0:
            # since all edges are positive the next_cost for src will never be less than 0
            next_cost[src] = 0
            # iterate over each edge
            for origin_city, dst_city, cost in flights:
                # if prev cost is infinity then we cna skip to next edge
                if prev_cost[origin_city] != maxsize:
                    # next_cost at current iteration
                    next_cost_dst = prev_cost[origin_city] + cost

                    # update next_cost arr if next_cost_dst is less than the cost in currently in next_cost array for dst
                    if next_cost_dst < next_cost[dst_city]:
                        next_cost[dst_city] = next_cost_dst

            # we've alredy reached the minimum cost, further iteration would not decrease cost any further
            if prev_cost == next_cost:
                break
            
            # set prev cost to next_cost for next iteration
            prev_cost = next_cost.copy()
            k -= 1

        return prev_cost[dst] if prev_cost[dst] != maxsize else -1


solution = Solution()
print(solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # 700
print(solution.findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1))  # -1
print(solution.findCheapestPrice(3, [[1,0,5]], 0, 1, 1))  # -1
print(solution.findCheapestPrice(7, [[0, 3, 7], [4, 5, 3], [6, 4, 8], [2, 0, 10], [6, 5, 6], [1, 2, 2], [2, 5, 9], [2, 6, 8], [3, 6, 3], [4, 0, 10], [4, 6, 8], [5, 2, 6], [1, 4, 3], [4, 1, 6], [0, 5, 10], [3, 1, 5], [4, 3, 1], [5, 4, 10], [0, 1, 6]], 2, 4, 1))
print(solution.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
