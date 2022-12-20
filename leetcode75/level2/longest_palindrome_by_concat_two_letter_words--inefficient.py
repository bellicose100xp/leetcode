from itertools import permutations
from typing import List

class Solution:
    
    def isPalindrome(self, word: str) -> bool:
        end: int = len(word) - 1
        start: int = 0

        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        
        return True

    def longestPalindrome(self, words: List[str]) -> int:
        """
        if n = num of 2-char strs in words list
        biggest combination = n x 2
        """
        n = len(words)
        
        while n > 0:
            perm: permutations[str] = permutations(words, n)

            while True:
                try:
                    words_tup: tuple[str] = next(perm)
                    word = ''.join(words_tup)
                    if (self.isPalindrome(word)):
                        return n*2
                except:
                    break
            
            n -= 1

        return 0

solution = Solution()
words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
print(solution.longestPalindrome(words))
