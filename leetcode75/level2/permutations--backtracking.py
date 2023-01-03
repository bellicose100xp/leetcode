from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations: list[list[int]] = []

        def backtrack(perm: list[int], remain: list[int]):
            if len(remain) == 0:
                permutations.append(perm[:])
                return
            
            _remain = remain[:]
            for num in _remain:
                perm.append(num)
                remain.remove(num)

                backtrack(perm, remain)

                perm.remove(num)
                remain.append(num)

        backtrack([], nums[:])
        return permutations

solution = Solution()
print(solution.permute([1,2,3]))