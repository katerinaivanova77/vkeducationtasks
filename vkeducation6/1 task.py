n = int(input())
nums = list(map(int, input().split()))
def long_cont(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1
    return max(dp)
print(long_cont(nums))

#Мы проходим массив один раз, делая только по одной проверке, соответственно, сложность будет O(n). Длина у нас хранится в массиве, соответсвенно именно по нему мы отслеживаем текущую и максимальную длину