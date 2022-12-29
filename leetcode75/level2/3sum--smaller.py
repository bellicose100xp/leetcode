from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()

        # Edge Case
        if len(nums) < 3:
            return 0

        triplets: int = 0

        for i in range(0, len(nums) - 2):
            num1: int = nums[i]
            _target = target - num1

            # 2sum with 2-pointer approach
            left: int = i + 1
            right: int = len(nums) - 1

            while left < right:
                num2 = nums[left]
                num3 = nums[right]
                _sum = num2 + num3

                if _sum < _target:
                    triplets += right - left  # all nums between left and right should be < _target for sorted arr
                    left += 1
                else:
                    right -= 1

        return triplets
