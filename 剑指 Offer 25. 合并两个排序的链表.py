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
                r = l1
                l1 = l1.next
            else:
                r.next = l2
                r = l2
                l2 = l2.next
        if l1:
            r.next = l1
        if l2:
            r.next = l2
        return head.next

l1 = ListNode(1)
l2 = ListNode(1)
l1.next = ListNode(2)
l2.next = ListNode(2)
s = Solution()
s.mergeTwoLists(l1,l2)