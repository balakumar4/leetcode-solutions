class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(map(s.count, set(s)))) == 1