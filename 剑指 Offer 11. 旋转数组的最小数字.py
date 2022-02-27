from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) // 2
            if numbers[mid] < numbers[left]:
                right = mid
            elif numbers[mid] > numbers[left]:
                left = mid + 1
            else:
                left += 1
        return numbers[left]