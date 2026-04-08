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
def mirtree(node):
    if node is None:
        return None
    node.left, node.right = node.right, node.left
    mirtree(node.left)
    mirtree(node.right)
    return node
def inorder_print(node):
    if node is None:
        return
    inorder_print(node.left)
    print(node.val, end=" ")
    inorder_print(node.right)
arr = []
for x in raw:
    if x == "None":
        arr.append(None)
    else:
        arr.append(int(x))
root = tree(arr)
print("Inorder до преобразования:")
inorder_print(root)
print()
mirtree(root)
print("Inorder после преобразования в зеркальное дерево:")
inorder_print(root)
print()

#Корректно работает, так как у каждого узла левый и правый потомки поменяли местами, затем рекурсивно делаем это для всех поддеревьев. Время O(n), память O(h)