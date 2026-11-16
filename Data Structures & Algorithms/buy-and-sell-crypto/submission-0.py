class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        we can track the minimum buy price from the left
        start at 0 index so 10 for example with profit = 0
        minBuy = prices[0]
        
        move 1 day ahead

        currSell = prices[i]
        track the running profit if we sold at the current day 
        so runningProfit = currSell - minBuy

        update profit to max(profit, runningProfit)
        update minBuy to equal min(minbuy, currSell)

        move 1 day ahead

        return profit
        """

        profit = 0

        for i in range(len(prices)):
            if i == 0:
                minBuy = prices[0]
            else:
                currSell = prices[i]
                runningProfit = currSell - minBuy
                profit = max(profit, runningProfit)
                minBuy = min(minBuy, currSell)
        
        return profit

