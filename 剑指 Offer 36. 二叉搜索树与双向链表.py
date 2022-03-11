class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def recur(root,pre):
            if root is None:
                return None
            root.left = recur(root.left,root)
            root.right = recur(root.right,root)
            if pre.val < root.val:
                while root.left is not None:
                    root = root.left
                root.left = pre
            elif pre.val > root.val:
                while root.right is not None:
                    root = root.right
                root.right = pre
            return root

        if not root:
            return None
        head = r = root
        while head.left is not None:
            head = head.left
        while r.right is not None:
            r = r.right
        root.right = recur(root.right,root)
        root.left = recur(root.left,root)
        head.left = r
        r.right = head
        return head


class Solution2:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            nonlocal pre,head
            if cur is None:
                return
            dfs(cur.left)
            if not pre:
                head = cur
            else:
                pre.right = cur
                cur.left = pre
            pre = cur
            dfs(cur.right)

        if not root:
            return
        head = pre = None
        dfs(root)
        head.left = pre
        pre.right = head
        return head
