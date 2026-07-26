class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            largest = 0
            for j in range(i + 1, len(arr)):
                if arr[j] > largest:
                    largest = arr[j]
            arr[i] = largest

        arr[len(arr) - 1] = -1
        return arr