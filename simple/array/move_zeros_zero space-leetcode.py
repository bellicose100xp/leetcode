class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Do it without using any extra space
            Parameters
                nums: list[int] -> A list of integers to rotate
            Return:
                None
        """
        ...

        zero_pointer: int = 0
        
        for i,n in enumerate(nums):
            if n != 0:
                nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]
                zero_pointer += 1

        print(nums)

        


solution = Solution()
solution.moveZeroes([0,1,0,3,12]) #? [1,3,12,0,0]