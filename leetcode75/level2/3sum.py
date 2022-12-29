from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output: set[tuple[int, int, int]] = set()

        nums.sort()

        for idx in range(0, len(nums) - 2):
            num1 = nums[idx]  # sum of the other two numbers must equal -num1

            # 2sum from here on
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                num2 = nums[left]
                num3 = nums[right]
                _sum = num2 + num3

                if _sum == -num1:
                    output.add(tuple(sorted([num1, num2, num3])))
                    left += 1
                    right -= 1
                elif _sum < -num1:
                    left += 1
                else:
                    right -= 1
            
        return [list(triplets) for triplets in output]

solution = Solution()
print(solution.threeSum([0,0,0]))