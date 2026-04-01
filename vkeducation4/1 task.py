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
def derevo(root):
    if root is None:
        return ["null"]
    result = [str(root.data)]
    result += derevo(root.left)
    result += derevo(root.right)
    return result
arr = mass(line)
root = tree(arr, 0)
print(" ".join(derevo(root)))

#Связь родитель-потомок задается через индексы в массиве, то есть по формулам,так как мы храним дерево в виде level-order, а структуры данных в данном случае массив и TreeNode