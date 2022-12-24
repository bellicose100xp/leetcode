from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def get_rotation_index(nums: list[int]) -> int:
            start = 0
            end = len(nums) - 1

            # list is not rotated
            if nums[start] < nums[end]:
                return 0

            while start <= end:
                mid = (start + end) // 2

                # if mid's next neighbor is less than mid, then we've found the rotate index
                if nums[mid] > nums[mid+1]:
                    return mid + 1
                
                if nums[mid] < nums[start]:
                    end = mid - 1 
                else:
                    start = mid + 1
            
            return 0

        def binary_search(start: int, end: int) -> int:
            while start <= end:
                mid = (start + end) // 2

                if nums[mid] == target:
                    return mid
                
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            
            return -1 

        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        rotation_index = get_rotation_index(nums)
        
        if rotation_index == 0:
            return binary_search(0, n - 1)

        if target < nums[0]:
             return binary_search(rotation_index, n - 1)
        
        return binary_search(0, rotation_index - 1)

solution = Solution()
print(solution.search([5,1,3], 0))  # -1
print(solution.search([4,5,6,7,0,1,2], 0))  # 4


        