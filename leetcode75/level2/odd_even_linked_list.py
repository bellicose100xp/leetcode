from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: Optional[ListNode]=None):
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
ll.insert_arr([1,2,3,4,5])

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base condition
        if head == None:
            return None
        elif head.next == None or head.next.next == None:
            return head

        original_end_pointer = head
        while original_end_pointer.next:
            original_end_pointer = original_end_pointer.next

    
        end = original_end_pointer
        curr: ListNode = head

        while curr is not None and curr.next != original_end_pointer and curr.next is not None and curr.next.next != original_end_pointer:
            assert curr.next is not None
            assert curr.next.next is not None
            next_curr: ListNode = curr.next.next  # get ref of next odd node
            even: ListNode = curr.next  # get ref to even node
            even.next = None  # set even's next_pointer to None
            end.next = even # set end's next pointer to even node above
            end = even  # move end's pointer to the even pointer as that's the last node in linked list now
            curr.next  = next_curr # set current node's next pointer to next odd node
            curr = curr.next  # move current pointer to next odd value
        
        if curr.next is not None and curr.next.next == original_end_pointer:
            assert curr.next.next is not None
            next_curr = curr.next.next
            even = curr.next
            even.next = None
            end.next = even
            curr.next = next_curr
        elif curr.next != None and curr.next == original_end_pointer:
            assert curr.next.next is not None
            next_node = curr.next.next
            even = curr.next
            even.next = None
            end.next = even
            curr.next = next_node
        
        return head

solution = Solution()

# solution modifies exisiting linked list so we can print the linked list afterwords
solution.oddEvenList(ll.head)
ll.print_ll()  # 1 -> 3 -> 5 -> 2 -> 4 -> None
