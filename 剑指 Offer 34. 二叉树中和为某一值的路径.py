from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        def dfs(root,sum):
            if root is None:
                return
            
            tmp.append(root.val)
            sum += root.val
            if sum == target and not root.left and not root.right:
                res.append(tmp[:])
            
            dfs(root.left,sum)
            dfs(root.right,sum)
            tmp.pop()

        res,tmp = [],[]
        dfs(root,0)
        return res