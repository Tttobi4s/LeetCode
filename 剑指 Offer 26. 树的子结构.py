class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return True
        return self.recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def recur(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.recur(A.left, B.left) and self.recur(A.right, B.right)
