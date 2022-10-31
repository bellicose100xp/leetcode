class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Do it without using any extra space
        """
        ...

        zeros: list[int] = []
        numbers: list[int] = []
        for i in nums:
            if i == 0:
                zeros.append(i)
            else:
                numbers.append(i)

        nums[:] = numbers + zeros

        print(nums)


solution = Solution()
solution.moveZeroes([0, 1, 0, 3, 12])  # ? [1,3,12,0,0]
