n, k = map(int, input().split())
nums = list(map(int, input().split()))
def subsum(nums, k):
    prefix_sum = 0
    count = 0
    prefix_count = {0: 1}
    for num in nums:
        prefix_sum += num
        need = prefix_sum - k
        if need in prefix_count:
            count += prefix_count[need]
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
    return count
print(subsum(nums, k))

#Сумма подмассива выражаем через разность двух префиксных сумм, поэтому вместо перебора границ мы просто проверяем словарь уже встреченных префиксных сумм