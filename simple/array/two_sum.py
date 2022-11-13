class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = len(nums)

        left_val_idx: int = 0
        right_val_idx: int = 0

        for idx, num in enumerate(nums):
            right_idx = idx + 1
            val_to_find = target - num

            for next_idx in range(right_idx, l):
                if nums[next_idx] == val_to_find:
                    left_val_idx = idx
                    right_val_idx = next_idx
                    break
        
        return [left_val_idx, right_val_idx]
                    


            

solution = Solution()
solution.twoSum([2,7,11,15], 9) #? [0, 1]
solution.twoSum([3,2,4], 6) #? [1, 2]
solution.twoSum([3,3], 6) #? [0, 1]
