from collections import defaultdict, Counter
from sys import maxsize

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter: Counter[str] = Counter(t)
        # uniq charcters in t_counter
        t_uniq_chars: int = len(t_counter)
        # w: current window being considered
        w_counter: defaultdict[str, int] = defaultdict(int)
        # uniq chars in curr window whose count is >= to corresponding chars count in t_counter 
        # whe t_uniq_chars == w_matched_chars, we have valid window
        w_matched_chars: int = 0

        # (minimum window found so far, left index of min window, right index of min window)
        min_win: tuple[int, int, int] = (-maxsize, -1, -1)

        left: int = 0
        right: int = 0

        while right < len(s):
            char = s[right]

            w_counter[char] += 1
            if w_counter[char] == t_counter[char]:
                w_matched_chars += 1
            
            while left <= right and w_matched_chars == t_uniq_chars:
                curr_window = right - left + 1
                
                if min_win[0] > curr_window:
                    min_win = (curr_window, left, right)

                char = s[left]
                w_counter[char] -= 1
                if t_counter[char] > 0 and w_counter[char] < t_counter[char]:
                    w_matched_chars -= 1

                left += 1
            right += 1
        
        return s[left:right+1]




    

