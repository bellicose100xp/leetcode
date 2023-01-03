from typing import List


class Solution:
    def __init__(self):
        self.combinations: set[tuple[int, ...]] = set()
        self.visited: set[tuple[tuple[int, ...], int]] = set()

    def dfs(self, summ: int, curr_comb: list[int], candidates: list[int], target: int):
        for num in candidates:
            summ += num
            curr_comb.append(num)
            sorted_curr_comb_tupl = tuple(sorted(curr_comb))
            visit_comb = (sorted_curr_comb_tupl, summ)

            if not visit_comb in self.visited:
                self.visited.add(visit_comb)

                if summ == target:
                    self.combinations.add(sorted_curr_comb_tupl)
                elif summ < target:
                    self.dfs(summ, curr_comb, candidates, target)

            summ -= curr_comb.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # combinations: set(tuple[int,...]) = set()
        curr_comb: list[int] = []

        self.dfs(0, curr_comb, candidates, target)

        return [list(tup) for tup in self.combinations]


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))  # [[2,2,3], [7]]
solution = Solution()
print(solution.combinationSum([2, 3, 5], 8))  # [[2,2,2,2], [2,3,3], [3,5]]
