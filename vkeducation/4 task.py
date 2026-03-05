input_str = input()
arr = list(map(int, input_str.split()))
def sortirovka(arr):
    left = 0
    right = len(arr)-1
    while left<right:
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] == 0:
            left += 1
        else:
            right -= 1

    return arr
result = sortirovka(arr)
print(result)