from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_len: int = 0
        left: int = 0
        right: int = 0
        mapper: defaultdict[str, int] = defaultdict(int)

        while right < len(s):
            c = s[right]
            mapper[c] += 1

            while mapper[c] > 1:
                left_c = s[left]
                mapper[left_c] -= 1
                left += 1
            
            max_sub_len = max(max_sub_len, right - left + 1)
            right += 1
        
        return max_sub_len

solution = Solution()
solution.lengthOfLongestSubstring("abcabcbb")  # ?
solution.lengthOfLongestSubstring("dvdf")  # ?
