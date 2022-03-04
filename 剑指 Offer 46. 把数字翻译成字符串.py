class Solution1:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a, b = 1, 1
        for i in range(1, len(s)):
            if '10' <= s[i - 1:i + 1] <= '25':
                a, b = b, a + b
            else:
                a, b = b, b
        return b


class Solution2:
    def translateNum(self, num: int) -> int:
        a, b = 1, 1
        y = num % 10
        while num >= 10:
            num //= 10
            x = num % 10
            if 10 <= (x * 10 + y) <= 25:
                a, b = b, a + b
            else:
                a, b = b, b
            y = x
        return b
