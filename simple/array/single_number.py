from collections import defaultdict

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d: dict[int, int] = defaultdict(int)
        uniquekey: float = float('inf')

        for num in nums:
            d[num] += 1
        
        for key, val in d.items():
            if val == 1:
                uniquekey = key
        
        return int(uniquekey)
        
solution = Solution()
solution.singleNumber([2,2,1]) #?
solution.singleNumber([4,1,2,1,2]) #?
solution.singleNumber([1]) #?


