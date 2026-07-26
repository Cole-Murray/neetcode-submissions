class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for num in nums:
            if num == val:
                x+=1

        for i in range(x):
            nums.remove(val)

        return(len(nums))

