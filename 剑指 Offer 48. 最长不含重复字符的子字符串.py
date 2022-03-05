class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {} 
        pre, res = 1, 0
        for i in range(len(s)):
            j = dict.get(s[i], -1) 
            dict[s[i]] = i 
            if i - j <= pre:
                pre = i - j
            else:
                pre = pre + 1
            res = max(res, pre)
        return res


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}  
        res, j = 0, -1
        for i in range(len(s)):
            if s[i] in dict:  
                j = max(dict[s[i]], j)  
            dict[s[i]] = i
            res = max(res, i - j) 
        return res
