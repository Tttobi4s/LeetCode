from typing import List


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            if target == nums[i]:
                res += 1
            elif target < nums[i]:
                return res
        return res


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > target - 1:
                right = mid
            else:
                left = mid + 1
        L = left
        left, right = 0, len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            left += 1
        return left - L


s = Solution2()
s.search([5, 7, 7, 8, 8, 10],8)
