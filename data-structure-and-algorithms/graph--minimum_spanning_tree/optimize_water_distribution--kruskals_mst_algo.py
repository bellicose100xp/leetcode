from typing import List


class Solution:
    def find(self, x: int, root: list[int]):
        if x == root[x]:
            return x
        root[x] = self.find(root[x], root)
        return root[x]

    def union(self, x: int, y: int, root: list[int], rank: list[int]):
        root_x = self.find(x, root)
        root_y = self.find(y, root)

        if root_x == root_y:
            return False

        if rank[root_y] > rank[root_x]:
            root[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            root[root_y] = root_x
        else:
            root[root_y] = root_x
            rank[root_x] += 1

        return True

    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ordered_edges: list[tuple[int, int, int]] = []

        # add the virtual node's edges (well's cost)
        for house, cost in enumerate(wells):
            ordered_edges.append((0, house + 1, cost))

        # add remaining edges (pipe's cost)
        for house1, house2, cost in pipes:
            ordered_edges.append((house1, house2, cost))

        # sort edges by cost
        ordered_edges.sort(key=lambda x: x[2])

        total_cost: int = 0
        root: list[int] = [i for i in range(n+1)]
        rank: list[int] = [1]*(n+1)
        joined: bool = False

        # iterate over all edges and join them using union-find fn
        for house1, house2, cost in ordered_edges:
            joined = self.union(house1, house2, root, rank)
            if joined:
                total_cost += cost

        return total_cost


solution = Solution()
print(solution.minCostToSupplyWater(3, [1, 2, 2],  [[1, 2, 1], [2, 3, 1]]))
