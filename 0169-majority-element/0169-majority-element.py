class Solution(object):
    def majorityElement(self, nums):
        count=0
        a=1
        for num in nums:
            if count==0:
                a=num
            if a == num :
                count +=1
            else:
                count -=1

        return a