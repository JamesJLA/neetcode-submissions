class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gain = 0
        for l in range(len(prices)):
            for r in range(l+1, len(prices)):
                diff = prices[r] - prices[l]
                if diff > gain:
                    gain = diff

        return gain