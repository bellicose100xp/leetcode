from collections import defaultdict, Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n: int = len(s)
        left: int = 0
        right: int = 0
        freq: defaultdict[str, int] = defaultdict(int)
        freq[s[right]] = 1
        max_freq: int = 1
        max_count: int = 0
        substr_len: int = 1

        while True:
            if substr_len - max_freq <= k:
                max_count = max(substr_len, max_count)
                right += 1
                
                if right == n:
                    break

                substr_len += 1
                freq[s[right]] += 1
                max_freq = Counter(freq).most_common(1)[0][1]
            else:
                freq[s[left]] -= 1
                left += 1
                substr_len -= 1
                max_freq = Counter(freq).most_common(1)[0][1]
        
        return max_count


solution = Solution()
print(solution.characterReplacement("AABABBA", 1))  # ? 4
solution.characterReplacement("ABAA", 0) #? 2
solution.characterReplacement("ABAB", 2) #? 4
solution.characterReplacement("AAAB", 0) #? 3
