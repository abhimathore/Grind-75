class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1 = 0
        left = 0
        right = 1
        
        while right < len(prices):
            curr_max = prices[right] -prices[left]
            if prices[left] < prices[right]:
                max1 = max(curr_max,max1)
            else:
                left = right
            right +=1
        return max1
                