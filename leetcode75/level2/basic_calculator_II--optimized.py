class Solution:
    def calculate(self, s: str) -> int:
        """
        T: O(n)
        S: O(1)
        """
        prev: int = 0
        curr: int = 0
        result: int = 0
        curr_operation: str = "+"

        i: int = 0
        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr*10 + int(s[i])
                    i += 1

                # go back one idx as we're past the numbers when the sub-while loop broke
                i -= 1
                if curr_operation == "+":
                    result += curr
                    prev = curr
                elif curr_operation == "-":
                    result -= curr
                    prev = -curr
                elif curr_operation == "*":
                    result -= prev
                    result += prev * curr
                    prev = prev * curr
                elif curr_operation == "/":
                    result -= prev
                    result += int(prev / curr)
                    prev = int(prev / curr)

            elif s[i] in ["+", "-", "*", "/"]:
                curr_operation = s[i]

            curr = 0
            i += 1
        
        return result

solution = Solution()
print(solution.calculate("42"))