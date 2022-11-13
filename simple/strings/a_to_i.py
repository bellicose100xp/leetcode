class Solution:
    def myAtoi(self, s: str) -> int:
        char_read: bool = False
            
        min_val: int = -2**31
        max_val: int = 2**31 - 1
            
        final_num_str: str = ""
        final_num: int = 0
        for c in s:         
            if not char_read:
                if c == " ":
                    continue
                elif c.isdigit() or c == "+" or c == "-":
                    final_num_str = c
                    char_read = True
                else:
                    break
            else:
                if c.isdigit():
                    final_num_str += c
                else:
                    break  
        
        try:
            final_num = int(final_num_str)
        except:
            final_num = 0
          
        final_num = min_val if final_num < min_val else final_num
        final_num = max_val if final_num > max_val else final_num
        
        return final_num
            
solution = Solution()
solution.myAtoi("42") #?
solution.myAtoi("4193 with words") #?
solution.myAtoi("   -42") #?