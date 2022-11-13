class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        found_num_dict: dict[int, int] = {}

        for idx, num in enumerate(nums):
            val_to_find: int = target - num

            if val_to_find in found_num_dict:
                return [found_num_dict[val_to_find], idx]

            found_num_dict[num] = idx

        return []


solution = Solution()
solution.twoSum([2, 7, 11, 15], 9)  # ? [0, 1]
solution.twoSum([3, 2, 4], 6)  # ? [1, 2]
solution.twoSum([3, 3], 6)  # ? [0, 1]
