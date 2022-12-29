from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # since output list should be unique and internal list order doesn't matter
        output: set[tuple[int, int, int]] = set()

        nums.sort()

        for idx in range(0, len(nums) - 2):
            num1 = nums[idx]  # sum of the other two numbers must equal -num1

            if idx != 0 and nums[idx] == nums[idx-1]:  # skip duplicates in 3sum
                idx += 1
            else:
                # 2sum - 2 pointer approach on sorted array
                left = idx + 1
                right = len(nums) - 1
                while left < right:
                    num2 = nums[left]
                    num3 = nums[right]
                    _sum = num2 + num3

                    if left != idx + 1 and nums[left] == nums[left - 1]: # skip duplicates in 2 sum
                        left += 1
                    elif _sum == -num1:
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