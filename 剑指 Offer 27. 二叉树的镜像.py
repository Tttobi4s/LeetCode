class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.right, root.left = self.mirrorTree(root.left), self.mirrorTree(root.right)
        return root

class Solution2:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            cur.left, cur.right = cur.right, cur.left
        return root

class Solution3:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            recur(root.left)
            recur(root.right)

        recur(root)
        return root
