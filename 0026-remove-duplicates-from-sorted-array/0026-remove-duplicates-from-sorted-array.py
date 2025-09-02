

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0  # pointer for last unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # found a new unique
                i += 1
                nums[i] = nums[j]
        
        return i + 1
