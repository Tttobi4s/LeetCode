class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow