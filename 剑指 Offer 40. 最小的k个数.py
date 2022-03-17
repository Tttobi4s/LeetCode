from typing import List


class Solution1:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quickSort(arr, l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            quickSort(arr, l, i - 1)
            quickSort(arr, i + 1, r)
        quickSort(arr, 0, len(arr) - 1)
        return arr[:k]


class Solution2:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr):
            return arr

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]:
                    j -= 1
                while i < j and arr[i] <= arr[l]:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i:
                return quick_sort(l, i - 1)
            if k > i:
                return quick_sort(i + 1, r)
            return arr[:k]
        return quick_sort(0, len(arr) - 1)
