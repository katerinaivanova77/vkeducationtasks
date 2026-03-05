arr = list(map(int, input().split()))
def duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
new_length = duplicates(arr)
print(f"Массив после удаления дубликатов: {arr[:new_length]}")