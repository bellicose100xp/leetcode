class Solution:
    def reverse(self, x: int) -> int:
        is_neg: bool = x < 0
        x_abs = abs(x)
        s = str(x_abs)
        s_rev = s[::-1]
        x_rev_abs = int(s_rev)
        x_rev = x_rev_abs*-1 if is_neg else x_rev_abs
        min_val = -2**31
        max_val = 2**31-1

        return x_rev if min_val < x_rev < max_val else 0


solution = Solution()
solution.reverse(12345)  # ?
solution.reverse(1534236469)  # ?
