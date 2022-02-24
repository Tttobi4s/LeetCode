class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        list_map = {}
        cur = head
        while cur:
            list_map[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            list_map[cur].random = list_map.get(cur.random)
            list_map[cur].next = list_map.get(cur.next)
            cur = cur.next
        return list_map[head]


class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        pre = head
        res = cur = head.next
        while cur.next:
            pre.next = cur.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None
        return res
