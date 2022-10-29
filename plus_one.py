class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
      num: int = int("".join([str(i) for i in digits]))
      num += 1
      return [int(i) for i in str(num)]
