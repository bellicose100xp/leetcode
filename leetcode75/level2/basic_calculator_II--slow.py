class Solution:
    def calculate(self, s: str) -> int:
        # multiplication -> Division -> Addition -> Subtraction
        operators: list[str] = ["+", "-", "*", "/"]
        arr: list[str] = []

        # create a array of seperated numbers and operators
        for c in s:
            if c == " ":
                continue

            if not arr:
                arr.append(c)
                continue

            if c not in operators:
                if arr[-1] in operators:
                    arr.append(c)
                else:
                    arr[-1] += c
            else:
                arr.append(c)
        
        # first pass: multiplication and division
        md_result: list[str | int] = []
        i: int = 0
        while i < len(arr):
            if arr[i] == '*':
                md_result[-1] = int(md_result[-1]) * int(arr[i+1])
                i += 2
            elif arr[i] == '/':
                md_result[-1] = int(int(md_result[-1]) / int(arr[i+1]))
                i += 2
            else:
                md_result.append(arr[i])
                i += 1

        # second pass: additional and subtration
        result: int = 0
        i = 0
        while i < len(md_result):
            if i == 0:
                result = int(md_result[i])
                i += 1
                continue
            
            if md_result[i] == '+':
                result += int(md_result[i+1])
                i += 2
            else:
                result -= int(md_result[i+1])
                i += 2
        
        return result
            

solution = Solution()
# print(solution.calculate("3+2*2"))
print(solution.calculate("0-2147483647"))