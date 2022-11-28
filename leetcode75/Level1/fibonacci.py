class Solution:
    def fib(self, n: int) -> int:
        
        def calc_fib(num: int) -> int:
            if num <= 1:
                return num
            
            return calc_fib(num-1) + calc_fib(num-2)

        return calc_fib(n)

solution = Solution()
solution.fib(4) #?