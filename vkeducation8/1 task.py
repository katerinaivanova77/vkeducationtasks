k = map(int, input().split())
arr = list(map(int, input().split()))
def maxsum(arr, k):
    if k <= 0 or k > len(arr):
        return None
    current_sum = 0
    for i in range(k):
        current_sum += arr[i]
    max_sum = current_sum
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)
    return max_sumn,
answer = maxsum(arr, k)
if answer is None:
    print("Некорректное k")
else:
    print(answer)

#Без этого алгоритма пришоось бы сохранять и считать предыдущую сумму, а со скользящим окном мы используем уже посчитанную сумму за O(n)