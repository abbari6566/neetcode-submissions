class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[right] < prices[left]:
                #found something strictly lower then left
                left = right
            else:
                cur_profit = prices[right] - prices[left]
                max_profit = max(max_profit, cur_profit)
            right += 1
        return max_profit

#Time - O(N)

'''
Another simple solution did before:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            curr_profit =price - min_price
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit
#time complexity - O(N) and space - O(1)
'''