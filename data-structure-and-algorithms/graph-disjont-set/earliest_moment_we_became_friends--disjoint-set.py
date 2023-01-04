from typing import List

class Solution:
    def find(self, root: list[int], x: int):
        if x == root[x]:
            return x
        root[x] = self.find(root, root[x])
        return root[x]

    def union(self, x: int, y: int, root: list[int], size: list[int]):
        root_x = self.find(root, x)
        root_y = self.find(root, y)

        if root_x == root_y:
            return 0

        if size[root_y] > size[root_x]:
            root[root_x] = root_y
        elif size[root_x] > size[root_y]:
            root[root_y] = root_x
        else:
            root[root_y] = root_x
            size[root_x] += 1

        return 1
    
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        root: list[int] = [i for i in range(n)]
        size: list[int] = [1]*n
        not_friends: int = n - 1
            
        logs.sort(key = lambda x: x[0])  # sort by time
        
        for time, x, y in logs:
            not_friends -= self.union(x, y, root, size)
            if not_friends == 0:
                return time
        
        return -1
            