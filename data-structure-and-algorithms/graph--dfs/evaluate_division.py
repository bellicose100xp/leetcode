from typing import List
from collections import defaultdict

class Solution:
    # backtracking
    def dfs(self, x: str, y: str, adj: dict[str, dict[str, float]], visited: set[str], acc_prod:float) -> float:
        visited.add(x)
        
        if y in adj[x]:
            return acc_prod * adj[x][y]
        
        for nei in adj[x]:
            if nei in visited:
                continue
            
            acc_prod *= adj[x][nei]
            product = self.dfs(nei, y, adj, visited, acc_prod)
            if product != -1:
                return product
            
            # backtrack accumalated product of last value
            acc_prod /= adj[x][nei]
            
        return float(-1)
            
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj: dict[str, dict[str, float]] = defaultdict(dict)
        
        # create adjacency matrix
        for (x, y), v in zip(equations, values):
            adj[x][y] = v
            adj[y][x] = 1 / v
        
        ret_arr: list[float] = []
            
        for x, y in queries:
            visited: set[str] = set()
            
            # returns x / y -> float if possible else -1
            product = self.dfs(x, y, adj, visited, 1)
            ret_arr.append(product)
            
        return ret_arr
            
            