input_str = input()
arr1 = list(map(int, input_str.split()))
input_str = input()
arr2 = list(map(int, input_str.split()))
def massive(arr1, arr2):
    a1 = len(arr1) - len(arr2) - 1
    a2 = len(arr2) - 1
    a = len(arr1) - 1

    while a2 >= 0:
        if a1 >= 0 and arr1[a1] > arr2[a2]:
            arr1[a] = arr1[a1]
            a1 -= 1
        else:
            arr1[a] = arr2[a2]
            a2 -= 1
        a -= 1

    return arr1
result = massive(arr1, arr2)
print(result)