class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = r = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                r.next = l1
                l1 = l1.next
            else:
                r.next = l2
                l2 = l2.next
            r = r.next
        r.next = l1 if l1 else l2
        return head.next