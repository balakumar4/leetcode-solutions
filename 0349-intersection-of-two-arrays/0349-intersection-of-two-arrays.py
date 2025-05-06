class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for c in nums1:
            if c in nums2:
                if c not in a:
                    a.append(c)
        return a


        