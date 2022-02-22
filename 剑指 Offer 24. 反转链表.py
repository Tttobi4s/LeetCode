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

class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur:
                return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res

        return recur(head, None)


