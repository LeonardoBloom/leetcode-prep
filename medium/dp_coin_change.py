def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1) 
    dp[0] = 0
    

    for i in range(1, len(dp)):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i-coin] + 1, dp[i] )
            print(dp)
    if dp[amount] != float('inf'):
        return dp[amount]
    else:
        return -1
    
print(coinChange([1,2,5], 11))


