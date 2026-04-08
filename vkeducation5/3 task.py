from collections import deque
import heapq
arr = list(map(int, input().split()))
k = int(input())
mode = input()
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
def kmin(arr, k):
    if k < 1 or k > len(arr):
        return None
    max_heap = []
    for value in arr:
        heapq.heappush(max_heap, -value)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]
def kmax(arr, k):
    if k < 1 or k > len(arr):
        return None
    min_heap = []
    for value in arr:
        heapq.heappush(min_heap, value)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
if mode == "min":
    answer = kmin(arr, k)
    print(f"{k}-й наименьший элемент:", answer)
elif mode == "max":
    answer = kmax(arr, k)
    print(f"{k}-й наибольший элемент:", answer)
else:
    print("Неверный режим")

#Память - O(k), так как почленно проходим кучу