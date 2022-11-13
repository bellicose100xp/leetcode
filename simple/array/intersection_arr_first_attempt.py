from collections import defaultdict, Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict1: dict[int, int] = dict(Counter(nums1))
        dict1 = defaultdict(lambda: 0, dict1)

        dict2: dict[int, int] = dict(Counter(nums2))
        dict2 = defaultdict(lambda: 0, dict2)

        uniq = set(nums1 + nums2)
        arr: list[int] = []

        for i in uniq:
            min_appearance = min(dict1[i], dict2[i])

            if min_appearance != 0:
                for _ in range(min_appearance):
                    arr.append(i)

        return arr


solution = Solution()
solution.intersect([1, 2, 2, 1], [2, 2])  # ? [2, 2]
solution.intersect([4, 9, 5], [9, 4, 9, 8, 4])  # ? [4, 9]
