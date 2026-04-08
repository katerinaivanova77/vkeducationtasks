from collections import deque
k = int(input())
arrays = []
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = 0
def tree(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = tree(arr, 2 * i + 1)
    root.right = tree(arr, 2 * i + 2)
    return root
import heapq
def mass(sorted_arrays):
    merged = []
    min_heap = []
    for array_index in range(len(sorted_arrays)):
        if len(sorted_arrays[array_index]) > 0:
            first_value = sorted_arrays[array_index][0]
            heapq.heappush(min_heap, (first_value, array_index, 0))
    while min_heap:
        value, array_index, element_index = heapq.heappop(min_heap)
        merged.append(value)

        next_index = element_index + 1
        if next_index < len(sorted_arrays[array_index]):
            next_value = sorted_arrays[array_index][next_index]
            heapq.heappush(min_heap, (next_value, array_index, next_index))
    return merged
for i in range(k):
    arr = list(map(int, input().split()))
    arrays.append(arr)
result = mass(arrays)
print("Объединенный отсортированный массив:")
print(*result)

#Время - O(NlogK), память - O(K) на кучу и O(N) на весь массив