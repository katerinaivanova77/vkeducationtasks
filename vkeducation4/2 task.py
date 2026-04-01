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
def mirror(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.data != b.data:
        return False
    return mirror(a.left, b.right) and mirror(a.right, b.left)
def symm(root):
    if root is None:
        return True
    return mirror(root.left, root.right)
arr = mass(line)
root = tree(arr, 0)
if symm(root):
    print("YES")
else:
    print("NO")

#Сравниваем левый узел левого дерева с правым узлом правого и наоборот, то есть проверяем деревья на зеркальность,алгоритм же работает корректно, так как мы сравниваем по уровням два дерева и на совпадение необходимых символов на каждом уровне