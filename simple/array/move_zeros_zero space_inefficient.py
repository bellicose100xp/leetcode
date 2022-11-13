class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Do it without using any extra space
        """
        ...

        for idx, val in enumerate(nums):
            if val == 0:
                continue
            else:
                left = idx-1
                right = idx
                while left >= 0 and nums[left] == 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left -= 1
                    right -= 1
        
        print(nums)

        


solution = Solution()
solution.moveZeroes([0,1,0,3,12]) #? [1,3,12,0,0]