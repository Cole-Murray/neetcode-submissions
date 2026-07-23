class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        max = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                curr = curr + 1
            else:
                curr = 0
            i += 1
            if curr > max:
                max = curr
        return max
