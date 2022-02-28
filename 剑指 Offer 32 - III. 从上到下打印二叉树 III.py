import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, res = collections.deque(), []
        queue.append(root)
        while queue:
            tmp = []
            for i in range(len(queue)):
                cur = queue.popleft()
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res

class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, res = collections.deque(), []
        queue.append(root)
        while queue:
            tmp = collections.deque()
            for i in range(len(queue)):
                cur = queue.popleft()
                if len(res) % 2:
                    tmp.appendleft(cur.val)
                else:
                    tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(list(tmp))
        return res
