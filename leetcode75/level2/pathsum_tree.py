from __future__ import annotations
from typing import List, Optional  # type: ignore
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class BinaryTree:
    def buildTreeLeetCode(self, arr: list[int | None]) -> TreeNode | None:
        # convert all values in arr to TreeNode(s)
        node_arr: list[TreeNode | None] = [TreeNode(val) if val else None for val in arr]

        n = len(node_arr)

        for idx, node in enumerate(node_arr):
            if node is None:
                continue

            next_left_idx = idx*2 + 1  # next left idx for current node
            next_right_idx = idx*2 + 2  # next right idx for current node

            # if next left index is greater then or equal to array length then break as we've reached the end of array
            if next_left_idx >= n:  
                break
            
            if node_arr[next_left_idx]:
                node.left = node_arr[next_left_idx]
            
            # if next right index is greater then or equal to array length then break as we've reached the end of array
            if next_right_idx >= n:  
                break

            if node_arr[next_right_idx]:
                    node.right = node_arr[next_right_idx]

        return node_arr[0]

# utility functions
def printTree(root: TreeNode | None) -> None:
    tree: str = ''
    queue: deque[TreeNode | None] = deque([root])

    while True:
        node = queue.pop()
        val = f'{node.val}' if node else 'None'
        tree += f'{val}'

        if node:
            queue.appendleft(node.left)
            queue.appendleft(node.right)

        if not queue or not any(queue):
            break
        else:
            tree += ' -> '

    print(tree)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count: int = 0

        def dfs_sum(root: TreeNode | None, sum: int):
            nonlocal count
            if root is None:
                return
            
            if root.left:
                left_sum = sum + root.left.val
                if left_sum == targetSum:
                    count += 1
                dfs_sum(root.left, left_sum)

            if root.right:
                right_sum = sum + root.right.val
                if right_sum == targetSum:
                    count += 1
                dfs_sum(root.right, right_sum)
        
        def dfs_traverse(root: TreeNode | None):
            nonlocal count
            
            if root is None:
                return
            
            val = root.val
            if val == targetSum:
                count += 1
            
            dfs_sum(root, val)

            if root.right:
                dfs_traverse(root.right)
            
            if root.left:
                dfs_traverse(root.left)
            
        
        dfs_traverse(root)
        return count

tree = BinaryTree()
leet = [5,4,8,11,None,13,4,7,2,None,None,5,1]
root = tree.buildTreeLeetCode(leet)
# printTree(root)

solution = Solution()
print(solution.pathSum(root, 22))