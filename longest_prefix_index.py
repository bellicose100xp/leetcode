class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        for i in range(200):
            char: str = ""
            for word in strs:
                if i >= len(word):
                    return result
                
                if char == "":
                    char = word[i]
                elif char == word[i]:
                    continue
                elif char != word[i]:
                    return result
            
            result += char
        return result

solution = Solution()
solution.longestCommonPrefix(["flower","flow","flight"]) #?