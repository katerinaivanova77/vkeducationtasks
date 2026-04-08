from collections import deque
import heapq
raw = input().split()
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
def balance(node):
    if node is None:
        return 0
    left_height = balance(node.left)
    right_height = balance(node.right)
    node.balance_factor = left_height - right_height
    return 1 + max(left_height, right_height)
def printbalance(node):
    if node is None:
        return

    printbalance(node.left)
    print(f"Узел {node.val}: balance_factor = {node.balance_factor}")
    printbalance(node.right)
arr = []
for x in raw:
    if x == "None":
        arr.append(None)
    else:
        arr.append(int(x))
root = tree(arr)
balance(root)
print("Balance factor для каждого узла:")
printbalance(root)

#Сначала вычисляем высоту поддеревьев, а потом обрабатываем текущий узел, используя post-order