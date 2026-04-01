line = input().strip()
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
def mass(line):
    tok = line.split()
    arr = []
    for token in tok:
        if token.lower() == "null":
            arr.append(None)
        else:
            arr.append(int(token))
    return arr
def tree(arr, i):
    if i >= len(arr):
        return None
    if arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = tree(arr, 2 * i + 1)
    root.right = tree(arr, 2 * i + 2)
    return root
def dep(root):
    if root is None:
        return 0
    q = deque()
    q.append((root, 1))
    while q:
        node, depth = q.popleft()
        if node.left is None and node.right is None:
            return depth
        if node.left is not None:
            q.append((node.left, depth + 1))
        if node.right is not None:
            q.append((node.right, depth + 1))
arr = mass(line)
root = tree(arr, 0)
print(dep(root))

#Поиск в ширину ведется по уровням, а значит первый лист, который встретим, будет лежать на минимальной глубине