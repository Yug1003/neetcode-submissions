class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        m=0

        for r in range(1 , len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                m = max(m , prices[r]-prices[l])

        return m