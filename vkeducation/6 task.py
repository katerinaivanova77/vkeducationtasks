int_str = input()
arr = list(map(int, int_str.split()))
def sortirovka(arr):
    num = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr.insert(num, arr.pop(i))
            num += 1
    return arr
result = sortirovka(arr)
print(result)