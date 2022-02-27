class Solution:
    def firstUniqChar(self, s: str) -> str:
        dict = {}
        for c in s:
            dict[c] = not c in dict
        for c in s:
            if dict[c]:
                return c
        return ' '
