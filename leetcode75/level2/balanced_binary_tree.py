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
    def calc_height(self, root: TreeNode | None) -> int:
            if root is None:
                return 0
            
            right = self.calc_height(root.right)
            left = self.calc_height(root.left)
            diff = abs(left - right)

             # return -1 immediately if any side is unbalanced or currnet node is unbalanced
            if right == -1 or left == -1 or diff > 1:
                return -1 
            
            # add current node's height (1) to max height of either side
            return max(right, left) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # return -1 indicates an unbalaned tree
        return self.calc_height(root) != -1

tree = BinaryTree()
leet = [3, 9, 20, None, None, 15, 7]
root = tree.buildTreeLeetCode(leet)
# printTree(root)

solution = Solution()
print(solution.isBalanced(root))