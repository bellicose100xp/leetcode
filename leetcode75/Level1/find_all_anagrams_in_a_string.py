from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s: int = len(s)
        len_p: int = len(p)

        if len_p > len_s:
            return []

        p_count: dict[str, int] = dict(Counter(p))
        s_count: dict[str, int] = {}
        found_idx: list[int] = []

        # rc: right_pointer_char, lc: left_pointer_char
        for right, rc in enumerate(s):
            left = right - len_p

            if left >= 0:
                lc = s[left]
                if lc in s_count:
                    s_count[lc] -= 1

            if rc in p_count:
                s_count[rc] = s_count.get(rc, 0) + 1
                if p_count == s_count:
                    found_idx.append(left + 1) 

        return found_idx

solution = Solution()
solution.findAnagrams("abab", "ab") #?