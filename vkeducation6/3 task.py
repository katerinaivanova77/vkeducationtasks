n = int(input())
coins = list(map(int, input().split()))
amount = int(input())
def coin(coins, amount):
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for current_sum in range(1, amount + 1):
        for coin in coins:
            if coin <= current_sum:
                dp[current_sum] = min(dp[current_sum], dp[current_sum - coin] + 1)
    if dp[amount] == INF:
        return -1
    return dp[amount]
print(coin(coins, amount))

#Это корректно, так как наше решение в любом случае заканчивается на некоторой монете, в связи с этим будут перебраны все варианты