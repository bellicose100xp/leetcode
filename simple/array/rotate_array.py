from collections import deque


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Rotate list of integers k times

            Parameters:
                nums (list[int]): A list of integers to rotate
                k (int): Number of times to rotate

            Return:
                None: Rotates the list in Place
        """
        deq = deque(nums)
        deq.rotate(k)
        print(deq)
        nums[:] = list(deq)
        print(nums)


solution = Solution()
solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)  # ?
solution.rotate([-1, -100, 3, 99], 2)  # ?
