from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reversePrint(self, head: ListNode) -> List[int]:
        new_head = ListNode(-1)
        new_head.next = None
        while head:
            node_temp = head.next
            head.next = new_head.next
            new_head.next = head
            head = node_temp
        res, p = [], new_head.next
        while p:
            res.append(p.val)
            p = p.next
        return res

class Solution2:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

class Solution3:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        else:
            return self.reversePrint(head.next) + [head.val]