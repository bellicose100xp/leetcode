from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
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
ll.insert_arr([4, 2, 1, 3])

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        arr: list[ListNode] = []
        curr: ListNode | None = head

        while curr:
            arr.append(curr)
            curr = curr.next
        
        arr.sort(key=lambda item: item.val)
        arr_len = len(arr)

        sorted_head: ListNode | None = arr[0]
        curr: ListNode | None = sorted_head

        for i in range(1, arr_len):
            curr.next = arr[i]
            curr = curr.next

        curr.next = None
        return sorted_head

solution = Solution()
head = solution.sortList(ll.head)
while head:
    print(head.val)
    head = head.next
