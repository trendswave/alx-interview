def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a large number
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still a large number, return -1
    return dp[total] if dp[total] != total + 1 else -1

# Example usage
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3 (5 + 5 + 1)
