class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        largest = -1
        for i in range(n - 1, -1, -1):
            ans[i] = largest
            if arr[i] > largest:
                largest = arr[i]
        return ans
            