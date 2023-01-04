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
            return True
        
        if size[root_y] > size[root_x]:
            root[root_x] = root_y
        elif size[root_x] >  size[root_y]:
            root[root_y] = root_x
        else:
            root[root_y] = root_x
            size[root_x] += 1
        
        return False
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # it's not a valid graph as a valid graph with N vertices will have n-1 edges.
        if len(edges) != n - 1: return False
        root: list[int] = [i for i in range(n)]
        
        # for union-by-rank optimization
        size: list[int] = [1]*n
        
        for edge in edges:
            x, y = edge
            cycle_found = self.union(x, y, root, size)
            
            if cycle_found:
                return False
        
        return True

soluton = Solution()
print(soluton.validTree(5, [[0,1],[0,2],[0,3],[1,4]])) # True
print(soluton.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])) # False