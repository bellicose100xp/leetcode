class Solution:
    def decodeString(self, s: str) -> str:
        """
        Time: O(n)
        Space: O(1)
        """
        stack: list[str] = []
        for c in s:
            if c.isalpha():
                if not stack or not stack[-1].isalpha():
                    stack.append(c)
                    continue
                stack[-1] = f"{stack[-1]}{c}"
            elif c.isnumeric():
                if not stack or not stack[-1].isnumeric():
                    stack.append(c)
                    continue
                stack[-1] = f"{stack[-1]}{c}"
            elif c == "[":
                stack.append(c)
            elif c == "]":
                # building substring
                sub = stack.pop()
                stack.pop()  # remove corresponding open bracket
                multiplier = int(stack.pop())
                sub = sub*multiplier
                if stack and stack[-1] != "[":
                    prev_found_strings = stack.pop()
                    sub = f"{prev_found_strings}{sub}"
                stack.append(sub)

        return stack[0]
            
solution = Solution()
solution.decodeString("3[a]2[bc]") #?
solution.decodeString("3[a2[c]]") #?
solution.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") #?