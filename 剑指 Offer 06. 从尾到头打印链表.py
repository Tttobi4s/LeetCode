from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

class Solution2:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        else:
            return self.reversePrint(head.next) + [head.val]