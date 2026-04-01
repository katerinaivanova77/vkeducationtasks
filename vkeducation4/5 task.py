line1 = input().strip()
line2 = input().strip()
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
def same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.data != b.data:
        return False
    return same_tree(a.left, b.left) and same_tree(a.right, b.right)
arr1 = mass(line1)
arr2 = mass(line2)
root1 = tree(arr1, 0)
root2 = tree(arr2, 0)
if same_tree(root1, root2):
    print("YES")
else:
    print("NO")

#Для того, чтобы деревья считались одинаковыми, необходимо совпадение по структуре и по значениями отдельных соотвествующих элементов