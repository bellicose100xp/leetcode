from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:

    if len(s) == 0:
        return 0

    mapper: defaultdict[str, int] = defaultdict(int)
    largest_substring: int = 0
    left: int = 0
    right: int = 0

    for i, c in enumerate(s):
        right = i
        mapper[c] += 1

        if mapper[c] == 2:
            prev_uniq_len = right - left
            if largest_substring < prev_uniq_len:
                largest_substring = prev_uniq_len

            while True:
                mapper[s[left]] -= 1

                if s[left] == c:
                    left += 1
                    break

                left += 1

    last_uniq_len = right - left + 1
    if largest_substring < last_uniq_len:
        largest_substring = last_uniq_len

    return largest_substring


lengthOfLongestSubstring("abcabcbb")  # ?
lengthOfLongestSubstring("dvdf")  # ?