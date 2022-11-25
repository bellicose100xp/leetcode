class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub_len: int = 0
        left: int = 0
        right: int = 0
        mapper: dict[str, int] = {}

        while right < len(s):
            c = s[right]
            
            if c not in mapper or (c in mapper and mapper[c] < left):
                mapper[c] = right
                max_sub_len = max(max_sub_len, right - left + 1)
            else:
                left = mapper[c] + 1
                mapper[c] = right

            right += 1
            
        return max_sub_len

solution = Solution()
solution.lengthOfLongestSubstring(" ")          #? 1
solution.lengthOfLongestSubstring("tmmzuxt")    #? 5
solution.lengthOfLongestSubstring("abba")       #? 2
solution.lengthOfLongestSubstring("abcabcbb")   #? 3
solution.lengthOfLongestSubstring("dvdf")       #? 3
