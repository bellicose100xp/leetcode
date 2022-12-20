from typing import List
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        map: defaultdict[str, int] = defaultdict(int)
        max_palindrome: int = 0
        for word in words:
            # rev: reversed string
            rev: str = word[::-1]

            if map[rev] != 0:
                map[rev] -= 1
                max_palindrome += 4
            else:
                map[word] += 1
        
        for key, val in map.items():
            if key[0] == key[1] and val != 0:
                return max_palindrome + 2
        
        return max_palindrome

solution = Solution()
words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
print(solution.longestPalindrome(words))
