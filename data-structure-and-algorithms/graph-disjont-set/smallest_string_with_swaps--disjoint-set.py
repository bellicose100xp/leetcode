from typing import List
from collections import defaultdict


class Solution:

    def find(self, x: int, root: list[int]) -> int:
        if x == root[x]:
            return x
        root[x] = self.find(root[x], root)
        return root[x]

    def union(self, x: int, y: int, root: list[int], rank: list[int]):
        root_x = self.find(x, root)
        root_y = self.find(y, root)

        if rank[root_x] > rank[root_y]:
            root[root_y] = root_x
        elif rank[root_y] > rank[root_x]:
            root[root_x] = root_y
        else:
            root[root_y] = root_x
            rank[root_x] += 1

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        _s: list[str] = list(s)
        n: int = len(_s)

        root: list[int] = [i for i in range(n)]
        rank: list[int] = [1]*n

        for x, y in pairs:
            self.union(x, y, root, rank)

        # Edge Case: Even with path compression and union-by-rank
        # some nodes may be pointing to a parent node
        # use self.find() to get root of all nodes in roots array

        root_only: list[int] = [self.find(x, root) for x in root]

        adj: defaultdict[int, list[int]] = defaultdict(list)

        for idx, root_node in enumerate(root_only):
            adj[root_node].append(idx)

        for root_node, indices in adj.items():

            chars: list[str] = []

            for idx in indices:
                chars.append(_s[idx])

            chars.sort()

            for c, idx in zip(chars, indices):
                _s[idx] = c

        return "".join(_s)


solution = Solution()
print(solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]))  # ? bacd
print(solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]]))  # ? abcd
print(solution.smallestStringWithSwaps("cba", [[0, 1], [1, 2]]))  # ? abc
