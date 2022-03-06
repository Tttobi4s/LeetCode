class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur is not None:
            if cur.val == val:
                pre.next = cur.next
                break
            pre = pre.next
            cur = cur.next
        return head
