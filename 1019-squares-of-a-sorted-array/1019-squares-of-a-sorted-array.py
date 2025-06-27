class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        o=[n*n for n in nums]
        o.sort()
        return o
