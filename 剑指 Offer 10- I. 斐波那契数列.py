class Solution1:
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


class Solution2:
    dict = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if Solution2.dict.get(n) is not None:
            return Solution2.dict[n]
        else:
            Solution2.dict[n] = self.fib(n - 1) + self.fib(n - 2)
        return Solution2.dict[n] % 1000000007


class Solution3:
    dp = [0, 1]

    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        for i in range(n - 1):
            Solution3.dp.append(Solution3.dp[i + 1] + Solution3.dp[i])
        return Solution3.dp[n] % 1000000007


class Solution4:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007
