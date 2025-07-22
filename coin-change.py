class Solution(object):
    def coinChange(self, coins, amount):
        dp= [float('inf')]*(amount+1)
        dp[0]=0

        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i and dp[i-coin] is not float('inf'):
                    dp[i]= min(dp[i], 1+dp[i-coin])

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

# https://leetcode.com/problems/coin-change/
