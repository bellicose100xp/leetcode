from collections import deque

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        deq: deque[int] = deque()
        l = len(digits)

        if digits[l-1] != 9:
            digits[l-1] += 1
            return digits

        if l == 1 and digits[0] == 9:
            return [1, 0]

        carryover: int = 0

        for i in range(l - 1, -1, -1):
            if i == l - 1:
                deq.append(0)
                carryover = 1
            elif digits[i] == 9 and carryover == 1:
                    if i == 0:
                        deq.appendleft(0)
                        deq.appendleft(1)
                    else:
                        deq.appendleft(0)
                        carryover = 1
            elif carryover == 1:
                deq.appendleft(digits[i] + 1)
                carryover = 0
            else:
                deq.appendleft(digits[i])

        return list(deq)

solution = Solution()
solution.plusOne([4,3,2,1]) #?
solution.plusOne([9,9,9]) #?
solution.plusOne([8,9,9,9]) #?
solution.plusOne([9,8,9]) #?