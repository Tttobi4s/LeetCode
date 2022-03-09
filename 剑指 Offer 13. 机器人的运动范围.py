import collections


class Solution1:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sums(number):
            s = 0
            while number:
                s += number % 10
                number //= 10
            return s

        def dfs(i, j, k):
            if not 0 <= i < m or not 0 <= j < n or (sums(i) + sums(j)) > k or (i, j) in dict:
                return 0
            dict.add((i, j))
            return 1 + dfs(i + 1, j, k) + dfs(i, j + 1, k)

        dict = set()
        return dfs(0, 0, k)


class Solution2:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sums(number):
            s = 0
            while number:
                s += number % 10
                number //= 10
            return s

        queue, dict = collections.deque(), set()
        queue.append((0, 0))
        while queue:
            i, j = queue.popleft()
            if 0 <= j < n and 0 <= i < m and sums(i) + sums(j) <= k and (i, j) not in dict:
                dict.add((i, j))
                for ni, nj in [(i + 1, j), (i, j + 1)]:
                    queue.append((ni, nj))
        return len(dict)