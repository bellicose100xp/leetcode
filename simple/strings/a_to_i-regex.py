import re

class Solution:
    def myAtoi(self, s: str) -> int:
        min_val: int = -2**31
        max_val: int = 2**31 - 1
            
        final_num_str = ""
        result = re.search(r'^\s*([+-]*[0-9]+)[^0-9]*', s)

        if result:
            final_num_str = result.group(1)

        try:
            final_num = int(final_num_str)
        except:
            final_num = 0
          
        if final_num < min_val:
            final_num = min_val
        elif final_num > max_val:
            final_num = max_val

        return final_num
            
solution = Solution()
solution.myAtoi("42") #?
solution.myAtoi("4193 with words") #?
solution.myAtoi("   -42") #?