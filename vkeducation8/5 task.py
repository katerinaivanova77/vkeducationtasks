n = int(input())
nums = list(map(int, input().split()))
def pivin(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1
print(pivin(nums))

#Префиксная сумма показывает баланс скобок, то есть если он отрицательный, значит закрывающихся скобок больше, а значит, такая последовательность не может быть правильной без удаления лишней открывающейся. Аналогично наоборот. За линейное время работает так как мы единожды проходим строку и совершаем некоторое счетное число операций.