class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[:n] + s[n:]

class Solution2:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = "" # 字符串：不可变类型，效率低，每次都要新建
        for i in range(n,len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res

class Solution3:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = [] # 列表：可变类型
        for i in range(n,len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return "".join(res)