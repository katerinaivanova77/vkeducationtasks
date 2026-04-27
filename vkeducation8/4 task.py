n = int(input())
arr = list(map(int, input().split()))
def rotin(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return left
print(rotin(arr))

#За каждый шаг отбрасываем примерно половину массива, то есть вместо линейного поиска получаем логарифмический