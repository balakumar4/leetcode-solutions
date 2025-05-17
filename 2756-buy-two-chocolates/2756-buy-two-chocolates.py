class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a=sorted(prices)
        b=a[0]+a[1]
        if b<=money:
            return money-b
        else:
            return money