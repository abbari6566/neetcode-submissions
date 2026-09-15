class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0]*(amount+1) #memo array 0-12 for amount = 12
        for i in range(1, amount+1):
          minimum = float('inf')
          for coin in coins:
              diff = i - coin
              if diff < 0:
                  break
              minimum = min(minimum, 1 + dp[diff])
          
          dp[i] = minimum
        
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1

# Bottom Up Appraoch
# Base case 0, building from 0 to amount
# Time - O(amount × numCoins)
'''
Once diff = i - coin goes negative, the code assumes every remaining coin in the list will also produce a negative diff, so it stops checking early. That assumption only holds if coins is sorted ascending — once you hit one coin bigger than i, all coins after it are guaranteed bigger too.
'''