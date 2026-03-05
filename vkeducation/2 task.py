input_str = input()
arr1 = list(map(int, input_str.split()))
arr1.sort()
input_str = input()
arr2 = list(map(int, input_str.split()))
arr2.sort()
def sorted_arrays(arr1, arr2):
    i = j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result
massive = sorted_arrays(arr1, arr2)
print(f'Результат слияния: {massive}')