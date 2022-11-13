class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = len(nums)

        left_val_idx: int = 0
        right_val_idx: int = 0

        for idx, num in enumerate(nums):
            val_to_find = target - num

            start_search_index = idx + 1 if idx < l-2 else l-1

            try:
                right_idx = nums.index(val_to_find, start_search_index)
            except:
                continue

            if right_idx != -1:
                left_val_idx = idx
                right_val_idx = right_idx
                break

        return [left_val_idx, right_val_idx]


solution = Solution()
solution.twoSum([2, 7, 11, 15], 9)  # ? [0, 1]
solution.twoSum([3, 2, 4], 6)  # ? [1, 2]
solution.twoSum([3, 3], 6)  # ? [0, 1]
