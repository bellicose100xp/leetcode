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


list1 = LinkedList()
list1.insert_arr([1, 2, 4])
# list1.print_ll()

list2 = LinkedList()
list2.insert_arr([1, 5, 8])
# list2.print_ll()


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None

        if list1 != None and list2 == None:
            return list1

        if list1 == None and list2 != None:
            return list2

        tail: Optional[ListNode] = None  # new list tail
        head: Optional[ListNode] = None  # new list head

        curr1: Optional[ListNode] = list1
        curr2: Optional[ListNode] = list2

        while curr1 != None or curr2 != None:
            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    if tail:
                        tail.next = curr1
                        tail = tail.next
                        curr1 = curr1.next
                    else:
                        tail = curr1
                        head = tail
                        curr1 = curr1.next
                else:
                    if tail:
                        tail.next = curr2
                        tail = tail.next
                        curr2 = curr2.next
                    else:
                        tail = curr2
                        head = tail
                        curr2 = curr2.next
            else:
                if curr1 and not curr2 and tail:
                    tail.next = curr1
                    return head
                elif not curr1 and curr2 and tail:
                    tail.next = curr2
                    return head

        return head


solution = Solution()
merged_list_head = solution.mergeTwoLists(list1.head, list2.head)

curr = merged_list_head
merged_list_string: str = ""

while curr:
    merged_list_string += f"{curr.val} -> "
    curr = curr.next

print(f"{merged_list_string} None")
