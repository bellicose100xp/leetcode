from collections import deque
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        @param nums: a list of integers to rotate
        @param k: num of steps to rotate by
        @return: None
        """
        deq = deque(nums)
        deq.rotate(k)
        print(deq)
        nums[:] = list(deq)
        print(nums)

solution = Solution()
solution.rotate([1,2,3,4,5,6,7], 3) #?
solution.rotate([-1,-100,3,99], 2) #?