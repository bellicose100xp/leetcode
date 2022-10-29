class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + digits


solution = Solution()
solution.plusOne([4, 3, 2, 1])  # ?
solution.plusOne([9, 9, 9])  # ?
solution.plusOne([8, 9, 9, 9])  # ?
solution.plusOne([9, 8, 9])  # ?
