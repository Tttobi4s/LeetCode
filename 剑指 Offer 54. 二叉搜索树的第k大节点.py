class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)

        res = []
        dfs(root)
        return res[-k]


class Solution2:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(cur):
            if not cur:
                return
            dfs(cur.right)
            self.k -= 1
            if self.k == 0:
                self.res = cur.val
                return
            dfs(cur.left)           

        self.k = k
        dfs(root)
        return self.res
