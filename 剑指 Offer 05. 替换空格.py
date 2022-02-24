class Solution1:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ':
                res.append('%20')
            else:
                res.append(c)
        return "".join(res)

class Solution2:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")

class Solutions:
    '''
    C++原地修改：
        遍历
        扩充数组
        双指针
        从后往前
    '''
