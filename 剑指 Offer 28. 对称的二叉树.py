class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def recur(A, B):
            if not A and not B:
                return True
            if not A or not B or A.val != B.val:
                return False
            return recur(A.left, B.right) and recur(A.right, B.left)

        return recur(root.left, root.right)
