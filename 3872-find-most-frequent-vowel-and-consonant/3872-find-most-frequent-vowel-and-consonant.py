class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel='aeiou'
        maxcount=0
        maxvowel=0
        for i in s:
            count=s.count(i)
            if i in vowel:
                if count>maxvowel:
                    maxvowel=count
            if i not in vowel:                   
                if count>maxcount:
                    maxcount=count
        return maxvowel+maxcount