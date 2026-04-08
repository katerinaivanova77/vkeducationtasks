from collections import deque
import heapq
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
def fulltree(root):
    if root is None:
        return True
    queue = deque([root])
    seen_null = False
    while queue:
        node = queue.popleft()
        if node is None:
            seen_null = True
        else:
            if seen_null:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True
raw = input().split()
arr = []
for x in raw:
    if x == "None":
        arr.append(None)
    else:
        arr.append(int(x))
root = tree(arr)
if fulltree(root):
    print("Дерево полное")
else:
    print("Дерево неполное")

#Данный способен удобен, так как мы проверяем заполненность по уровням слева направо, что и делает BFS