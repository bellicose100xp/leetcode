class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr: list[int] = []

        n1: list[int] = sorted(nums1)
        len1 = len(n1)

        n2: list[int] = sorted(nums2)
        len2 = len(n2)

        l, r = 0, 0

        while l < len1 and r < len2:
            left = n1[l]
            right = n2[r]

            if left == right:
                arr.append(left)
                l += 1
                r += 1
            elif left < right:
                l += 1
            elif left > right:
                r += 1

        return arr


solution = Solution()
solution.intersect([1, 2, 2, 1], [2, 2])  # ? [2, 2]
solution.intersect([4, 9, 5], [9, 4, 9, 8, 4])  # ? [4, 9]
