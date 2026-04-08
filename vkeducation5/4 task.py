from collections import deque
import heapq
raw = input().split()
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
def kmin(root, k):
    stack = []
    current = root
    count = 0
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.right
    return None
def kmax(root, k):
    stack = []
    current = root
    count = 0
    while stack or current:
        while current:
            stack.append(current)
            current = current.right
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.left
    return None
arr = []
for x in raw:
    if x == "None":
        arr.append(None)
    else:
        arr.append(int(x))
root = tree(arr)
if mode == "min":
    answer = kmin(root, k)
    print(f"{k}-й наименьший элемент в BST:", answer)
elif mode == "max":
    answer = kmax(root, k)
    print(f"{k}-й наибольший элемент в BST:", answer)
else:
    print("Неверный режим")

