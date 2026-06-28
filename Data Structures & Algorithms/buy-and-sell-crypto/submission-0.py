class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        for right in range(1,len(prices)):
            m=min(prices[:right])
            r=prices[right]-m
            ans=max(r,ans)
        return ans    
        