input_str = input()
arr = list(map(int, input_str.split()))
k = int(input())
def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
def sdvig(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    return arr
result = sdvig(arr, k)
print("Результат после сдвига на {k}: {result}")