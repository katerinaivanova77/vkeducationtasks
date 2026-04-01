line = input().strip()
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
def min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.data
def max(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.data
def max_min(root):
    if root is None:
        return -1
    mn = min(root)
    mx = max(root)
    return mn * mx
arr = mass(line)
root = tree(arr, 0)
print(max_min(root))

#Для нахождения минимального и максимального значения мы по сути двигаемся по одной выбранной ветке, соответственно проходим путь длиной h, отсюда и такая сложность