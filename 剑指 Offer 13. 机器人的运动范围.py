class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        dict = set()

        def sums(number):
            s  = 0
            while number:
                s += number % 10
                number //= 10
            return s
        
        def dfs(i,j,k):
            if not 0 <= i < m or not 0 <= j < n or (sums(i) + sums(j)) > k or (i,j) in dict:
                return 0
            dict.add((i,j))          
            return 1 + dfs(i + 1, j, k) + dfs(i, j + 1, k)
 
        return dfs(0,0,k)