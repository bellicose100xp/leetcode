from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sums: int = sum(nums)

        if num_sums % 2 == 1:
            return False

        half: int = int(num_sums / 2)

        def dfs(idx: int, summ: int, nums: list[int]) -> bool:
            if summ == 0:
                return True
            
            if summ < 0 or idx == len(nums):
                return False
            
            return dfs(idx + 1, summ, nums) or dfs(idx + 1, summ - nums[idx], nums)

        return dfs(0, half, nums)



