class Solution1:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])


class Solution2:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i, aList = len(s) - 1, []
        while i >= 0:   
            while s[i] == ' ': i -= 1
            j = i
            while j >= 0 and s[j] != ' ':
                j -= 1
            aList.append(s[j + 1:i + 1]) 
            i = j - 1         
        return " ".join(aList)
