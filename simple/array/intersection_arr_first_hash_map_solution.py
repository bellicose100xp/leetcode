class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr: list[int] = []
        dict1: dict[int, int] = {}

        for i in nums1:
            dict1[i] = dict1.get(i, 0) + 1

        for i in nums2:
            if dict1.get(i, 0) > 0:
                dict1[i] -= 1
                arr.append(i)

        return arr


solution = Solution()
solution.intersect([1, 2, 2, 1], [2, 2])  # ? [2, 2]
solution.intersect([4, 9, 5], [9, 4, 9, 8, 4])  # ? [4, 9]
