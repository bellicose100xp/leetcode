from __future__ import annotations  # postponed evaluation of annotations
from typing import Optional


class ListNode:  # Definition for singly-linked list.
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: ListNode | None = None
        self.last: ListNode | None = None

    def insert(self, val: int):
        new_node: ListNode | None = ListNode(val)
        if self.head == None:
            self.head = new_node
            self.last = self.head
        else:
            last_node: ListNode | None = self.last
            if last_node is not None:
                last_node.next = new_node
            self.last = new_node

    def print_ll(self):
        cur: ListNode | None = self.head
        ll_str = ""
        if cur != None:
            ll_str: str = f'{str(cur.val)} -> '
            while cur.next:
                cur = cur.next
                ll_str += f'{str(cur.val)} -> '
            ll_str += "None"
        print(ll_str)

    def insert_arr(self, arr: list[int]):
        for val in arr:
            self.insert(val)


ll = LinkedList()
ll.insert_arr([1,2,3,2,1])
# ll.print_ll()


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l: int = 0
        curr: Optional[ListNode] = head
        while curr:
            l += 1
            curr = curr.next

        mid: int = l // 2
        skip: int = -1 if l % 2 == 0 else mid + 1

        stack: list[int] = []
        curr = head
        counter: int = 1

        while curr:
            if counter != skip:
                if counter <= mid:
                    stack.append(curr.val)
                elif curr.val != stack.pop():
                    return False
                    
            curr = curr.next
            counter += 1

        return True

solution = Solution()
print(solution.isPalindrome(ll.head))