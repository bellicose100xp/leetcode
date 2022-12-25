from __future__ import annotations
from typing import List, Optional  # type: ignore

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # base case #1
        if not nums:
            return None
    
        end = len(nums) - 1
        
        # base case #2
        if end == 0:
            return TreeNode(nums[0])
        
        mid = end // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root