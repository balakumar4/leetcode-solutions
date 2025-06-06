class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        a=set(nums)
        for i in nums:
            if i !=max(a) and i !=min(a):
                return i
        return -1    


        