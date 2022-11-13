from __future__ import annotations  # postponed evaluation of annotations

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
ll.insert_arr([1, 2, 3, 4, 5])
ll.print_ll()
