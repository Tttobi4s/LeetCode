class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[:n] + s[n:]

class Solution2:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = ""
        for i in range(n,len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res

class Solution3:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n,len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return "".join(res)