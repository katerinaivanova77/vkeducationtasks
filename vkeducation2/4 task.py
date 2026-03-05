a = input()
b = input()
from collections import deque
def sovpadenie(a, b):
    q = deque()
    for el in a:
        q.append(el)
    for el in b:
        if q and q[0] == el:
            q.popleft()
    return len(q) == 0
if sovpadenie(a, b):
    print(f"Список {a} является исходным для {b}")
else:
    print(f"Список {a} не является исходным для списка {b}")