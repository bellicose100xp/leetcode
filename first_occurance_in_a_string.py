import re

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = re.search(needle, haystack)
        if result:
            return result.start()
        return -1
        