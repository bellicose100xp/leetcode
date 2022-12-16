import itertools

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return 0 is either number is zero
        if num1 == "0" or num2 == "0":
            return "0"

        # reverse number so it's easier to iterate through the digits in reverse order
        first: str = num1[::-1]
        second: str = num2[::-1]

        # multiply each num in second with all nums in first and add the result to array
        sum_arr: list[str] = []
        for idx, sec_num in enumerate(second):
            sum_arr.append("0"*idx)  # add 0 based in the num index of the second
            carry: int = 0
            for first_num in first:
                temp_sum: int = ( int(first_num) * int(sec_num) ) + carry
                digit = temp_sum % 10
                carry = temp_sum // 10
                sum_arr[idx] = f'{sum_arr[idx]}{digit}'
            
            if carry:
                sum_arr[idx] = f'{sum_arr[idx]}{carry}'
        
        result: str = ''

        for num in sum_arr:
            temp_result: str = ''
            carry: int = 0
            # zip longest will pad "0" to match the longest string if needed
            for n1, n2 in itertools.zip_longest(result, num, fillvalue="0"):
                temp_sum: int = int(n1) + int(n2) + carry
                digit = temp_sum % 10
                carry = temp_sum // 10
                temp_result = f'{temp_result}{digit}'

            if carry:
                temp_result = f'{temp_result}{carry}'
            
            result = temp_result
        
        return result[::-1]

solution = Solution()
print(solution.multiply("123", "456"))  # OUTPUT: 56088