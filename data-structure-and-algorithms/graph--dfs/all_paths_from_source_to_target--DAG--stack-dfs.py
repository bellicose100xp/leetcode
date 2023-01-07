from typing import List

class Solution:     
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        stack: list[list[int]] = [[0]]
        output: list[list[int]] = []
        curr_path:list[int]  = []
            
        while stack:
            curr_path = stack.pop()
            
            if curr_path[-1] == target:
                output.append(curr_path[:])
                continue
            
            for nei in graph[curr_path[-1]]:
                next_path = curr_path[:]
                next_path.append(nei)
                stack.append(next_path)
            
        return output

solution = Solution()
print(solution.allPathsSourceTarget([[1,2],[3],[3],[]]))