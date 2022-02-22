class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode(-1)
        new_head.next = None
        while head:
            node_temp = head.next
            head.next = new_head.next
            new_head.next = head
            head = node_temp
        return new_head.next

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
