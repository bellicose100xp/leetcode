from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations: list[list[int]] = []

        def backtrack(target: int, curr_comb: list[int], start_idx: int):
            if target == 0:
                combinations.append(curr_comb[:])
                return
            
            if target < 0:
                return
            
            for i in range(start_idx, len(candidates)):
                num = candidates[i]
                curr_comb.append(num)
                backtrack(target - num, curr_comb, i)
                curr_comb.pop()  # backtrack from 'num' before exploring another path
        
        backtrack(target, [], 0)
        return combinations


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))  # [[2,2,3], [7]]
print(solution.combinationSum([2, 3, 5], 8))  # [[2,2,2,2], [2,3,3], [3,5]]
