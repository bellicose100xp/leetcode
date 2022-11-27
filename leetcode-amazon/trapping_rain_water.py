class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time: O(2n)
        Space: O(n)
        """
        
        # return 0 if the number of height blocks is less than 2 as you need a minimum of 3 blocks to hold water
        n = len(height)
        if n <= 2:
            return 0
        
        water_saved: int = 0
        max_left: int = 0
        max_right: int = 0

        
        # create a dictionary of right indexes with the maximum values to their right
        # Time: O(n), Space: O(n)
        max_right_dict: dict[int, int] = {}
        max_right_val = 0
        for i in range(n-2, 0, -1):
            curr_val = height[i+1]
            max_right_val = max(curr_val, max_right_val)
            max_right_dict[i] = max_right_val
        
        # Time: O(n), Space O(1)
        for i in range(1, n-1):
            curr: int = height[i]
                
            max_left = max(height[i-1] , max_left)
            max_right = max_right_dict[i]
                
            water_stored_by_curr = min(max(max_left, curr), max(max_right, curr)) - curr
            water_saved += water_stored_by_curr
        
        return water_saved
                