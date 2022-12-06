class Solution:
    def next_num(self, n: int):
        total: int = 0
        while n != 0 :
            digit = n % 10
            total += digit ** 2
            n = n // 10
        return total

    def isHappy(self, n: int) -> bool:
        s: set[int] = set()
        while n != 1 and n not in s:
            s.add(n)
            n = self.next_num(n)

        return n == 1

solution = Solution()
solution.isHappy(19) #?