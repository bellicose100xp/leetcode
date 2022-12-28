from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sums: int = sum(nums)

        if num_sums % 2 == 1:
            return False

        half: int = int(num_sums / 2)

        def dfs(summ: int, nums: list[int] ) -> bool:
            nonlocal half

            if summ == half:
                return True
            
            if summ > half or not nums:
                return False

            result: bool = False
            
            for num in nums:
                remain: list[int] = nums[:]
                remain.remove(num) # create a copy of array with nums removed
                output = dfs(summ+num, remain)
                if output == True:
                    result = True

            return result

        return dfs(0, nums)