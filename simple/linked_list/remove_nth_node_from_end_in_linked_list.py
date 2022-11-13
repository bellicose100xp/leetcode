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
# ll.insert_arr([1, 2])


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        node: ListNode | None = head
        pointer: ListNode | None = head
        lag: int = 1
        trailing_pointer: ListNode | None = head

        if head != None and head.next == None:
            return None

        while True:
            if node != None and node.next:
                node = node.next
                if n - lag <= 0 and pointer != None:
                    pointer = pointer.next
                if n - lag < 0 and trailing_pointer != None:
                    trailing_pointer = trailing_pointer.next
                lag += 1
            else:
                break

        if head != None and head.next != None and pointer != None and trailing_pointer != None and trailing_pointer.next != None:  # for python typing: asserting that values are not None
            if head.next == pointer and pointer == node:
                trailing_pointer.next = None
            elif pointer == head:
                head.val = head.next.val
                head.next = head.next.next
            else:
                trailing_pointer.next = trailing_pointer.next.next

        return head


solution = Solution()
solution.removeNthFromEnd(ll.head, 2)
ll.print_ll()
