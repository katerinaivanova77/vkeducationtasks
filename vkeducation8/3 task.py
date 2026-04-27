n = int(input())
nums = list(map(int, input().split()))
def length(nums):
    prefix_sum = 0
    max_len = 0
    first_position = {0: -1}
    for i in range(len(nums)):
        if nums[i] == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1
        if prefix_sum in first_position:
            current_len = i - first_position[prefix_sum]
            max_len = max(max_len, current_len)
        else:
            first_position[prefix_sum] = i
    return max_len
print(length(nums))

#После замены 1 и 0 на 1 и -1 сумма подмассива с одинаковым числом 1 и 0 изначально будет 0, тогда задача сведется к поиску самого длинного подмассива с суммой 0