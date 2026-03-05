input_str = input()
arr = list(map(int, input_str.split()))
def sortirovka(arr):
    left = 0
    mid = 0
    right = len(arr)-1
    while mid <= right:
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid +=1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
    return arr
result = sortirovka(arr)
print(result)